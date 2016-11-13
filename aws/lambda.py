import subprocess
import cPickle as pickle

def lamba_handler(event, context):
	pickle.dump(event, open("/tmp/event.p","wb"))
	args = ("venv/bin/pyth3.4 ","python3_thingamee.py")
	popen = subprocess.Popen(args, stdout=subprocess.PIPE)
	popen.wait()
	output = popen.stdout.read()
	print(output)
