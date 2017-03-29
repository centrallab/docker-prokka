from app.celeryapp import app
import os
import os.path


def format_cmd(prog, flags, arg):
    a = list(map(lambda x: x[0] + "=" + str(x[1]) if x[1] != "" else x[0], flags))
    flag = " ".join(a)
    return " ".join([prog, flag, arg])


@app.task
def prokka(filename, file):
    with open(os.path.join("/input", filename), "w") as f:
        f.write(file)

    name, ext = filename.split(".")
    output_dir = os.path.join("/output", name)
    args = list()
    args.append(("--cpus", "2"))
    args.append(("--outdir", output_dir))
    args.append(("--prefix", name))
    cmd = format_cmd("prokka", args, os.path.join("/input", filename))
    os.system(cmd)

    filepath = os.path.join(output_dir, name)
    with open("{}.ffn".format(filepath), "r") as f:
        ffn_file = f.read()
    with open("{}.gff".format(filepath), "r") as f:
        gff_file = f.read()
    result = [("{}.ffn".format(name), ffn_file), ("{}.gff".format(name), gff_file)]

    os.system("rm -r {}".format(output_dir))
    return result
