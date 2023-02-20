from .celery import app
from time import sleep
from datetime import datetime
from decimal import Decimal,getcontext


@app.task
def add(x, y):
    # sleep(10)
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print("Current Time =", current_time)
    # print( x , "New -->" )
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task
def pi_calc():
    sleep(1)
    pi_val = 100
    return pi_val 
                
                
# adding watchdog - enable refersh with every change

#watchdog auto-restart --directory=./proj --pattern=*.py --recursive -- celery -A proj worker --concurrency=1 --loglevel=INFO --pool=solo

# execute regulary 
#celery -A proj worker --pool=solo -l INFO