from subprocess import run, PIPE, Popen

def ping(address, count = 1, ):
    result = run(f'ping /n {count} {address} ', stdout=PIPE, stderr=PIPE, universal_newlines=True)
    print(result.returncode, result.stdout, result.stderr)
    return result.returncode == 0 and ('Destination host unreachable.' not in result.stdout)

def pin1(address, count = 1, ):
    result = run(f'ping -w 1 -c {count} {address}',shell= True,stdout=PIPE, stderr=PIPE, universal_newlines=True)
    print(result.returncode, result.stdout, result.stderr)
    return result.returncode == 0

def shut_down1():
    cmdCommand = "shutdown -h now"
    return Popen(cmdCommand.split(), stdout=PIPE)

def shut_down():
    print("SHUTDOWN")
