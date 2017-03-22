from app.tasks import add, prokka
import os
import time

if __name__ == '__main__':
    print("sleep for 10 sec")
    time.sleep(10)
    results = []
    for name in os.listdir("/input"):
        result = prokka.delay(name)
        results.append(result)
    
    while all(map(lambda x: x.ready(), results)):
        time.sleep(2)
    #for i in range(10):
    #    result = add.delay(1, 2)
    #    print('Task finished?', result.ready())
    #    print('Task result:', result.result)
    #    time.sleep(2)
    #    print('Task finished"', result.ready())
    #    print('Task result:', result.result)
