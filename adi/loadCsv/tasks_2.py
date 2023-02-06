
from .worker import app
import logging
logger = logging.getLogger(__name__)

@app.task(bind=True, name='test_load')  
def test_load(self, x):
        print("Hi", x)
        return x


@app.task(bind=True, name='a')  
def a(self, x):
        print("a", x)
        return x
