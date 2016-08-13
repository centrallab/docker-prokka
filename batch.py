import sys
import os
import multiprocessing

proc_num = int(sys.argv[1])
cmds = map(lambda x: x.replace("'", ""), sys.argv[2:])

pool = multiprocessing.Pool(proc_num)
for cmd in cmds:
    pool.apply(os.system, args=(cmd, ))
pool.close()
pool.join()


