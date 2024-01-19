import os
import glob
import numpy as np
import mdtraj as md
all_pdb = glob.glob('complex*/*.pdb')
pep1_dist=[]
pep2_dist=[]
whole=open('base.fasta').readlines()[-1].strip()
colon=[]
for i in range(len(whole)):
    if whole[i]==':':
        colon.append(i)

pep1=whole[:colon[0]]
prot=whole[colon[0]+1:colon[1]]
pep2=whole[colon[1]+1:]

pep1_pair=[]
for i in range(len(pep1)):
    for j in [len(pep1)+41,len(pep1)+42,len(pep1)+43]:
        pep1_pair.append([j,i])

#print(pep1_pair)

pep2_pair=[]
for i in range(len(prot)+len(pep1),len(whole)-2):
    for j in [len(pep1)+41,len(pep1)+42,len(pep1)+43]:
        pep2_pair.append([j,i])

#print(pep2_pair)
for i in all_pdb:
    a=md.load(i)
    dist = md.compute_contacts(a, pep1_pair, scheme='CA')[0]
    pep1_dist.append(np.mean(dist))
for i in all_pdb:
    a=md.load(i)
    dist = md.compute_contacts(a, pep2_pair, scheme='CA')[0]
    pep2_dist.append(np.mean(dist))

#print(pep1_dist)
#print(pep2_dist)

count=0
for i,j in zip(pep1_dist, pep2_dist):
    if i > j:
        count+=1
print("{} {:.2f}".format(os.getcwd().split('/')[-1], count))
