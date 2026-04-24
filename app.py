from flask import Flask, render_template, request, redirect, url_for
from src import gcalendar
import gettext
import os
import datetime
import sys
import getopt

def main(argv):
    try:
        # 'p:' means -p requires a value
        opts, args = getopt.getopt(argv, "l:", ["param="])
    except getopt.GetoptError:
        sys.exit(2)
    _ = setup_localization("it")
    for opt, arg in opts:
        if opt in ("-l", "--language"):
            # Set up localization
            print(f"Received parameter: {arg}")
            _ = setup_localization(arg)


app = Flask(__name__)

@app.template_filter('format_date')
def format_date_filter(value):
    if value is None:
        return ""
    # 2026-04-24T13:24:00Z
    return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").strftime('%d-%m-%Y %H:%M')

@app.template_filter('translate')
def translate_filter(value):
    if value is None:
        return ""
    return _(value)

# Set up localization
def setup_localization(language):
    # Define the path to the locale directory
    localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
    print(localedir)
    # Install the selected language
    translation = gettext.translation('messages', localedir, languages=[language], fallback=True)
    translation.install()
    
    # Return the translation function
    return translation.gettext


# Sample tasks for demonstration
cal = gcalendar.google_calendar()

@app.route('/')
def index():
    return render_template('index.html', tasks=cal.get_events(5))

@app.route('/add', methods=['POST'])
def add_task():
    task_title = request.form.get('title')
    task_description = request.form.get('description')
    task_when = request.form.get('when')
    task_email = request.form.get('email')
    print(f'task_email:{task_email}')
    cal.add_event(task_title, task_description, task_when)
    return redirect(url_for('index'))

@app.route('/complete', methods=['POST'])
def complete_tasks():
    completed_tasks = request.form.getlist('taskCheckbox')
    for index in map(int, completed_tasks):
        if 1 <= index <= len(cal.get_events):
            cal.get_events[index - 1] += " - Completed"
    return redirect(url_for('index'))

# Add a new route to handle task deletion
@app.route('/delete', methods=['POST'])
def delete_tasks():
    tasks_to_delete = request.form.getlist('taskCheckbox')
    tasks_to_delete.sort(reverse=True)  # Start deleting from the end to avoid index issues
    for index in map(int, tasks_to_delete):
        if 1 <= index <= len(cal.get_events):
            cal.delete_event(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # For now, hardcode to Spanish for testing
    main(sys.argv[1:])
    print(_("Attendees"))
    app.run(port=8000, debug=True)

