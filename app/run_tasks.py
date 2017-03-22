from app.tasks import add
import time

if __name__ == '__main__':
    for _ in range(10):
        result = add.delay(1, 2)
        print('Task finished?', result.ready())
        print('Task result:', result.result)
        time.sleep(2)
        print('Task finished"', result.ready())
        print('Task result:', result.result)
