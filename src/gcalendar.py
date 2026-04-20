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
        startDate = datetime.datetime.strptime(input_date, "%d/%m/%Y %H:%M").date()
        endDate = startDate - datetime.timedelta(minutes=30)
        event = {
            'summary': title,
            # 'location': '800 Howard St., San Francisco, CA 94103',
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

        return self.service.events().insert(calendarId='primary', body=event).execute() 
    
    def get_events(self, howMany):
        # Call the Calendar API
        now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
        print("Getting the upcoming 10 events")
        events_result = (
            self.service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=howMany,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            return

        # Prints the start and name of the next 10 events
        return events
        # for event in events:
        #  start = event["start"].get("dateTime", event["start"].get("date"))
    def delete_event(self, event_id):
        event = self.service.events().delete(calendarId='primary', eventId=event_id).execute()
        print(f"Event {event['id']} modified successfully.")