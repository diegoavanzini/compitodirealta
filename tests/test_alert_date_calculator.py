from src.alert_date import alert_date_calculator
from datetime import datetime
import time
import pytest

def test_alert_date():
    assert alert_date_calculator("12/04/2026") == "11/04/2026"

def test_input_date_is_old():
    old_input_date = datetime.now()
    time.sleep(1)
    with pytest.raises(ValueError, match="Date cannot be in the past"):
        alert_date_calculator(old_input_date.strftime("%d/%m/%Y"))