##Gene Symbol to Parser
import os
from Bio import Entrez
Entrez.email = 'sshah28@luc.eud'
os.chdir('/home/shyam/Documents/WGCNA')
Organism = '"Mus Musculus"'
ids = []
a=[]
#####
f = open('GeneSymbols.csv','r')
line = f.readline().rstrip()
i =0
while line != '':
    line = line.rstrip(',')
    ids += [line]
    line = f.readline().rstrip()
    i=i+1
####
d ={}
for it in ids:
    stringIDs = '(' + it + '[sym]) AND ' +Organism
    handle = Entrez.esearch(db="gene", term=stringIDs)
    record = Entrez.read(handle)
    gi_list = record["IdList"]
    print gi_list
    a += [(gi_list)]
    if ',' in str(gi_list):
        d[it] = gi_list
f.close()
f=open('SymboltoEntrez.csv','r')
j = 0
while j < i:
    line = ids[j] + ',' + a[j] + '\n'
    f.write(line)
    j += 1
for it in d:
    k = d[it]
    for iz in k:
        handle = Entrez.esummary(db='gene',id=iz)
        record = Entrez.read(handle)
        name = record['DocumentSummarySet']['DocumentSummary'][0]['NomenclatureSymbol']
        if name == it:
            break
    d[it]= iz

for it in d:
    iz = d[it]
    handle = Entrez.esummary(db='gene',id=iz)
    record = Entrez.read(handle)
    name = record['DocumentSummarySet']['DocumentSummary'][0]['NomenclatureSymbol']
    if name != it:
            print str(it)
j =0
f.close()
f=open('FixedEntrez.csv','w')

while j<i:
    name = ids[j]
    if (d.has_key(name) == True):
        k = d[name]
    else:
        k = a[j]
    k = ''.join(k)
    line = str(name) + ',' + str(k) + '\n'
    f.write(line)
    j+=1

    
