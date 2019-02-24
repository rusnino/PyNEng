import subprocess

reply = subprocess.run(['ping', '-c', '3', '-n', '3.8.8.8'], stdout=subprocess.DEVNULL)

if reply.returncode == 0:
    print('Alive')
else:
    print('Unreachable')
