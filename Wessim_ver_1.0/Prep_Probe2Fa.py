import sys

def main(argv):
	if len(argv) < 1:
		usage()
	probefile = argv[0]
	f = open(probefile)
	w = open(probefile + ".fa", 'w')
	line = f.readline()
	line = f.readline()
	while line:
		values = line.split("\t")
		if len(values) < 3:
			line = f.readline()
			continue
		target = values[0]
		seqid = values[1]
		seq = values[2]
		w.write(">" + seqid + "-" + target + "\n")
		w.write(seq + "\n")
		line = f.readline()
	f.close()
	w.close()

def usage():
	print ">Python Prep_Probe2Fa.py probe.txt"
	sys.exit()


if __name__=="__main__":
	main(sys.argv[1:])
