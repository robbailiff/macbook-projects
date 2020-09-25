import csv


with open('livermore1a.txt', encoding='latin-1') as tsvfile:
	#tsvfile.decode('utf-8', 'replace')
	for line in csv.reader(tsvfile, dialect="excel-tab"):
		print(line)

#reader = csv.reader(tsvfile, delimiter='\t')

#for row in reader:
	#print(row)


