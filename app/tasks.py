from app.celeryapp import app
import os
import os.path
import time

def format_cmd(prog, flags, arg):
    a = list(map(lambda x: x[0] + "=" + str(x[1]) if x[1] != "" else x[0], flags))
    flag = " ".join(a)
    return " ".join([prog, flag, arg])

@app.task
def add(x,y):
    time.sleep(1)
    return x+y

@app.task
def prokka(filename):
    name, ext = filename.split(".")
    args = list()
    args.append(("--cpus", "2"))
    args.append(("--outdir", os.path.join("/output", name)))
    args.append(("--prefix", name))
    cmd = operations.format_cmd("prokka", args, os.path.join("/input", filename))
    os.system(cmd)
    
