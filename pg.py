import os,subprocess
def func(ask):
    def run(cmd):
            completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
            return completed
    def conv(x):
        other = x.split("/")
        length = len(other)
        for i in range(length):
            if " " in other[i]:
                other[i] = "'{}'".format(other[i])
        return '/'.join(other)
    s = ask
    extra = ""
    if '.' in s:
        fname,ext = s.split(".")
    else:
        fname,ext = s,''
        extra = 'start '
    direc = 'cd /'
    lis = (os.popen(f'{direc} && dir /s /b {fname}?.{ext}').read())
    mainlis = lis.split("\n")
    test = extra+mainlis[0].replace("\\","/")
    run(test)
    print(test)
