import sys

infile_name = sys.argv[1]
outfile_name = sys.argv[2]
filter_by = sys.argv[3]

logfile = open(infile_name, 'r')
outfile = open(outfile_name, 'w')

for line in logfile:
    if line.find(filter_by) != -1:
        outfile.write(line)

logfile.close()
outfile.close()
