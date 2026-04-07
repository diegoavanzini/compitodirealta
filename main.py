import sys
from src.alert_date import alert_date_calculator

if len(sys.argv) >= 2:
    try:
        input_date = sys.argv[1]
        ad =  alert_date_calculator(input_date)
        print(ad)
    except  ValueError as e:
        print(f"Please provide a valid alert date as a command-line argument.{e}")
else:
    print("Please provide the alert date as a command-line argument.")

