import sys
import os
import argparse

MINIDENTITY = "90"
MINSCORE = "100"

def main(argv):
	parser = argparse.ArgumentParser(description='Blat Search for probe hybridization in Wessim2', prog='Prep_BlatSearch', formatter_class=argparse.RawTextHelpFormatter)
	group1 = parser.add_argument_group('Mandatory input files')
	group1.add_argument('-R', metavar = 'FILE', dest = 'reference', required=True, help = '2bit formatted reference file')
	group1.add_argument('-P', metavar = 'FILE', dest = 'probe', required=True, help = 'FASTA format probe sequence file generated from Prep_Probe2Fa')
	group2 = parser.add_argument_group('Search options')
	group2.add_argument('-i', metavar = 'INT', dest = 'minidentity', required=False, help = 'Min-identity for blat match [90]', default="90")
	group2.add_argument('-s', metavar = 'INT', dest = 'minscore', required=False, help = 'Min-Score for blat match [100]', default="100")
	group3 = parser.add_argument_group('Output options')
	group3.add_argument('-o', metavar = 'FILE', dest = 'outfile', required=False, help = 'Output file name [Probe_File_Name.psl]', default='')

	args = parser.parse_args()
	ref = args.reference
	probefile = args.probe
	outfile = args.outfile
	if outfile=='':
		outfile = probefile + ".psl"
	MINIDENTITY = args.minidentity
	MINSCORE = args.minscore
	
	serverStopCommand = "gfServer stop localhost 6666"
	serverStartCommand = "gfServer start -canStop localhost 6666 " + ref
	blatCommand = "gfClient localhost 6666 / -minIdentity=" + MINIDENTITY + " -minScore=" + MINSCORE + " " + probefile + " " + outfile
#	print serverStopCommand
#	os.system(serverStopCommand)
#	print serverStartCommand
#	os.system(serverStartCommand)
	print blatCommand
	os.system(blatCommand)


def usage():
	print ">python Prep_BlatSearch.py ref.2bit probes.txt.fa output.psl"
	sys.exit()

if __name__=="__main__":
	main(sys.argv[1:])
