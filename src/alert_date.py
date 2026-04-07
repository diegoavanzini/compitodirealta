from datetime import datetime, timedelta

def alert_date_calculator(input_actual_date):
    actual_date = datetime.strptime(input_actual_date, "%d/%m/%Y")
    if actual_date < datetime.now():
        raise(ValueError("Date cannot be in the past"))
    alert_date = actual_date - timedelta(days=1)
    return alert_date.strftime("%d/%m/%Y")
