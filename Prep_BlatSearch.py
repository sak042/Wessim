import sys
import os


MINIDENTITY = "90"
MINSCORE = "100"

def main(argv):
	if len(argv) < 3:
		usage()
	ref = argv[0]
	probefile = argv[1]
	outfile = argv[2]
	serverStopCommand = "gfServer stop localhost 6666"
	serverStartCommand = "gfServer start -canStop localhost 6666 " + ref
	blatCommand = "gfClient localhost 6666 / -minIdentity=" + MINIDENTITY + " -minScore=" + MINSCORE + " " + probefile + " " + outfile
	print serverStopCommand
#	os.system(serverStopCommand)
	print serverStartCommand
#	os.system(serverStartCommand)
	print blatCommand
	os.system(blatCommand)


def usage():
	print ">python x2.blatprobes.py ref.2bit probes.fa output.psl"
	sys.exit()

if __name__=="__main__":
	main(sys.argv[1:])
