from app.celeryapp import app
import time


@app.task
def add(x, y):
    print("long time task begins")
    time.sleep(1)
    print("long time task finished")
    return x + y
    
