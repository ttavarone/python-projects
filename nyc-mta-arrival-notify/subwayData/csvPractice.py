import csv

stops = open('stops.csv')
reader = csv.reader(stops)
outputFile = open('output.txt', 'w', newline='')
outputWriter = csv.writer(outputFile)
for row in reader:
	#print(str(reader.line_num)+str(row))
	outputWriter.writerow(row)
outputFile.close()