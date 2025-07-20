import csv, os

firstFile = True
csvRows = []
EXTENSION = '.csv'
ENCODING = 'utf8'
SEPERATOR = '\t'

os.makedirs('merged', exist_ok=True)
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith(EXTENSION):
        continue  # skip non-csv files
    print('Merging ' + csvFilename + '...')
    csvFileObj = open(csvFilename, encoding=ENCODING, newline='')
    readerObj = csv.reader(csvFileObj, delimiter=SEPERATOR)

    for row in readerObj:  # Read rows
        if readerObj.line_num == 1:
            if not firstFile:
                continue  # skip first row
            elif firstFile:
                firstFile = False  # read first row of first file, not read other first rows
        csvRows.append(row)
    csvFileObj.close()

# Write out the CSV file.
csvFileObj = open(os.path.join('merged', 'merged' + EXTENSION), 'w', newline='', encoding=ENCODING)
csvWriter = csv.writer(csvFileObj, delimiter=SEPERATOR)
for row in csvRows:
    csvWriter.writerow(row)
csvFileObj.close()
