import os.path
import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

class google_calendar():
    """classe per collegarsi a Google Calendar"""
    def __init__(self):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open("token.json", "w") as token:
                    token.write(creds.to_json())
        try:
            self.service = build("calendar", "v3", credentials=creds)
        except HttpError as error:
            print(f"An error occurred: {error}")

    def add_event(self, title, description, input_date):
        cdrCalendarId = self.create_calendar_if_not_exists("cdr")
        startDate = datetime.datetime.strptime(input_date, "%d/%m/%Y %H:%M")

        endDate = startDate + datetime.timedelta(minutes=30)
        event = {
            'summary':  title,
            'location': 'via Della Castella, 14 26100 Cremona',
            'description': description,
            'start': {
                'dateTime':  startDate.strftime("%Y-%m-%dT%H:%M:%S-02:00"), 
                'timeZone': 'Europe/Rome',
            },
            'end': {
                'dateTime': endDate.strftime("%Y-%m-%dT%H:%M:%S-02:00"),
                'timeZone': 'Europe/Rome',
            },
            'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=1'
            ],
            'attendees': [
                {'email': 'd.avanzini@teamsystem.com'},
                # {'email': 'iacopo.avanzini@gmail.com'},
                # {'email': 'paolettafilomena@gmail.com'},
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        return self.service.events().insert(calendarId=cdrCalendarId, body=event).execute() 
    
    def get_events(self, howMany):
        # Call the Calendar API
        cdrCalendarId = self.create_calendar_if_not_exists("cdr")
        now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
        print("Getting the upcoming 10 events")
        events_result = (
            self.service.events()
            .list(
                calendarId=cdrCalendarId,
                timeMin=now,
                maxResults=howMany,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        # Prints the start and name of the next 10 events
        return events
        # for event in events:
        #  start = event["start"].get("dateTime", event["start"].get("date"))
    def create_calendar_if_not_exists(self, calendar_summary, time_zone='UTC'):
        # 1. List all calendars
        calendars_result = self.service.calendarList().list().execute()
        calendars = calendars_result.get('items', [])
        
        # 2. Check if a calendar with the given summary already exists
        for calendar in calendars:
            if calendar.get('summary') == calendar_summary:
                print(f"Calendar '{calendar_summary}' already exists with ID: {calendar['id']}")
                return calendar['id']
        
        # 3. If not found, create a new calendar
        new_calendar = {
            'summary': calendar_summary,
            'timeZone': time_zone
        }
        created_calendar = self.service.calendars().insert(body=new_calendar).execute()
        print(f"Created new calendar '{calendar_summary}' with ID: {created_calendar['id']}")
        return created_calendar['id']        
    def delete_event(self, event_id):
        event = self.service.events().delete(calendarId='primary', eventId=event_id).execute()
        print(f"Event {event['id']} modified successfully.")