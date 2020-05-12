# Copyright (c) 2020 Liam R Mitchell. Released under MIT License.

#########################
####### imports #########
#########################
import argparse

#########################
##### default args ######
#########################
THREADS = 8

#########################
######## parser #########
#########################

def build_parser():
	parser = argparse.ArgumentParser()
	#required
	parser.add_argument('-i','--input',dest='indir',help='the directory which will store the input',metavar='INDIR',required=True)
	parser.add_argument('-o','--output',dest='outdir',help='the directory which will store the output',metavar='OUTDIR',required=True)
	parser.add_argument('-r','--reference',dest='ref',help='uniquely-renamed reference file',metavar='REFERENCE',required=True)
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-l','--illumina', action = 'store_true')
	group.add_argument('-n','--nanopore', action = 'store_true')
	#optional
	parser.add_argument('--threads',type=int,dest='threads', help='number of threads to use',metavar='THREADS',default=THREADS)
	return parser

########################
###### functions #######
########################

def handle_directories(i,o):
	if not os.path.exists(i):
		sys.exit("that's an invalid input directory")
	if not os.path.exists(o):
		os.makedirs(o)

	aldir=o+"/alignments/"
	rodir=o+"/finalout/"

	if not os.path.exists(aldir):
		os.makedirs(aldir)
	if not os.path.exists(rodir):
		os.makedirs(rodir)

	return aldir,fodir




########################
######### main #########
########################

def main():
	parser = build_parser()
	options = parser.parse_args()

	print(options)

	[aligndir,finaldir] = handle_directories(indir,outdir)


if __name__ == '__main__':
	main()

