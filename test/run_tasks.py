from prokkaapp.tasks import prokka
import os
import time


def check_ready(async_results):
    deleted = []
    for r in async_results:
        if r.ready():
            for filename, file in r.get():
                print(filename)
                with open(os.path.join("/output", filename), "w") as f:
                    f.write(file)
            deleted.append(r)
    for d in deleted:
        async_results.remove(d)


if __name__ == '__main__':
    print("sleep for 10 sec")
    time.sleep(10)
    results = []
    for name in os.listdir("/input"):
        filename = os.path.join("/input", name)
        with open(filename, "r") as f:
            result = prokka.s(name, f.read()).apply_async()
        results.append(result)

    time.sleep(60)

    while results:
        time.sleep(10)
        check_ready(results)
