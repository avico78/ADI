from .celery import app
from time import sleep
from datetime import datetime


@app.task
def add(x, y):
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("AAAAAAA Current Time =", current_time)
    print("I-->", x ,y )
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


# adding watchdog - enable refersh with every change

#watchmedo auto-restart --directory=./proj --pattern=*.py --recursive -- celery -A proj worker --concurrency=1 --loglevel=INFO --pool=solo

# execute regulary 
#celery -A proj worker --pool=solo -l INFO