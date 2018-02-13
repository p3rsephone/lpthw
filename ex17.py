from sys import argv
from os.path import exists

script, fileSource, fileDest = argv

inFile = open(fileSource)
inputData = inFile.read()

print(f"The input file is {len(inputData)} bytes long")

print(f"Checking if the output file exists... {exists(fileDest)}")
if not exists(fileDest):
    print(f"Creating file {fileDest}...")
outFile = open(fileDest, 'w+')

print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

outputData = outFile.write(inputData)
inFile.close()
outFile.close()

print("Done!")
