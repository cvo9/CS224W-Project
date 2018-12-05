import csv

networkFile = "DCh-Miner_miner-disease-chemical.tsv"
dbFile = "structure links.csv"

drugs = set([])
allDBIDs = set([])

index = 0
with open(networkFile) as new:
	for line in csv.reader(new, delimiter="\t"):
		# Ignore header
		if index == 0:
			index += 1
			continue

		dbID = line[1]
		drugs.add(dbID)

		index += 1

index = 0
with open(dbFile) as new:
	for line in csv.reader(new, delimiter=","):
		# Ignore header
		if index == 0:
			index += 1
			continue

		dbID = line[0]
		name = line[1]
		smiles = line[6]
		
		if smiles != "":
			allDBIDs.add(dbID)

		index += 1

print "Drugs:", len(drugs)
print "All DB IDs:", len(allDBIDs)

numInCommon = 0
for drug in drugs:
	if drug in allDBIDs:
		numInCommon += 1

print "Num Drugs w/ Valid DB ID:", numInCommon