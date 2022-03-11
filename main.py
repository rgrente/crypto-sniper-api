import subprocess

process = subprocess.Popen('./test.sh',stdout=subprocess.PIPE)
while True:
    output = process.stdout.readline()
    if process.poll() is not None and output == '':
        break
    if output:
        print (output.strip())
retval = process.poll()