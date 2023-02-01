
from .worker import app

@app.task(bind=True, name='load_csv')  
def load_csv(self,url):  
    return "Hi"

