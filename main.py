from src.alert_date import alert_date_calculator
from src.data_file import write_on_file, read_file

try:
    action = input("cosa vuoi fare? \n1. per aggiungere un nuovo compito \n2. per vedere i compiti presenti\n")
    if action == "1":
        title = input("get the title:")
        description = input("get the description:")
        input_date = input("get the date:")
        ad =  alert_date_calculator(input_date)
        print()
        # print(input_date + ";" + ad + ";" + title + ";" + description)
        write_on_file("compiti.txt", ad + ";" + title + ";" + description)
        print(f"new event added. You will be alerted on {ad}")
    else: 
        print()
        print(read_file("compiti.txt"))
    print()
except  ValueError as e:
    print(f"Please provide a valid date: {e}")
except  FileNotFoundError as e:
    print("no events")  
