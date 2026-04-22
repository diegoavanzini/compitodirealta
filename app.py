from flask import Flask, render_template, request, redirect, url_for
from src import gcalendar
import datetime

app = Flask(__name__)

# Sample tasks for demonstration
cal = gcalendar.google_calendar()

@app.route('/')
def index():
    return render_template('index.html', tasks=cal.get_events(5))

@app.route('/add', methods=['POST'])
def add_task():
    new_task = request.form.get('newTask')
    if new_task:
        startDate = datetime.datetime.now() + datetime.timedelta(days=1)
        when = startDate.strftime("%d/%m/%Y %H:%M")
        cal.add_event(new_task, new_task, when )
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
    app.run(port=8000, debug=True)