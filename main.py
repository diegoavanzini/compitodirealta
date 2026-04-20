import shelve
from src import gcalendar

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def main():
    cal = gcalendar.google_calendar()
    
    action = input("cosa vuoi fare? \n1. per aggiungere un nuovo compito \n2. per vedere i compiti presenti\n(q per uscire)\n")
    if action == "q":
       exit(0)
    if action == "1":
        title = input("get the title:")
        description = input("get the description:")
        input_date = input("get the date (dd/mm/yyyy hh:mm):")

    inserted_event = cal.add_event(title, description, input_date)
    print(f"Event created: {inserted_event}")

    db = shelve.open('events')

    print(f"Event from db: {db[title]}")

    db.close()
    



if __name__ == "__main__":
  main()
# [END calendar_quickstart]

# try:
#     action = input("cosa vuoi fare? \n1. per aggiungere un nuovo compito \n2. per vedere i compiti presenti\n")
#     if action == "1":
#         title = input("get the title:")
#         description = input("get the description:")
#         input_date = input("get the date:")
#         ad =  alert_date_calculator(input_date)
#         print()
#         # print(input_date + ";" + ad + ";" + title + ";" + description)
#         write_on_file("compiti.txt", ad + ";" + title + ";" + description)
#         print(f"new event added. You will be alerted on {ad}")
#     else: 
#         print()
#         print(read_file("compiti.txt"))
#     print()
# except  ValueError as e:
#     print(f"Please provide a valid date: {e}")
# except  FileNotFoundError as e:
#     print("no events")  
