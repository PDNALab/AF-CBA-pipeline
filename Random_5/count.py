import os
import glob
import numpy as np
import mdtraj as md
all_pdb = glob.glob('complex*/*.pdb')
pep1_dist=[]
pep2_dist=[]
whole=open('../../base.fasta').readlines()[-1].strip()
colon=[]
for i in range(len(whole)):
    if whole[i]==':':
        colon.append(i)

pep1=whole[:colon[0]]
prot=whole[colon[0]+1:colon[1]]
pep2=whole[colon[1]+1:]

def ref(keys,pep1,complx):
    min_dist=[]
    for key in keys:
        pep_pair=[]
        for i in range(len(pep1)):
            for j in [len(pep1)+key]:
                pep_pair.append([j,i])
        a=md.load(complx)
        dist = md.compute_contacts(a, pep_pair, scheme='CA')[0]
        min_dist.append(dist.min())
    return np.mean(min_dist)

def comp(keys,pep1, complx):
    min_dist=[]
    for key in keys:
        pep_pair=[]
        for i in range(len(prot)+len(pep1),len(whole)-2): 
            for j in [len(pep1)+key]:
                pep_pair.append([j,i])
        a=md.load(complx)
        dist = md.compute_contacts(a, pep_pair, scheme='CA')[0]
        min_dist.append(dist.min())
    return np.mean(min_dist)

for i in all_pdb:
    dist1=ref([41,42,43],pep1,i)
    dist2=comp([41,42,43],pep2,i)
    pep1_dist.append(dist1)
    pep2_dist.append(dist2)
count=0
for i,j in zip(pep1_dist, pep2_dist):
    if i > j:
        count+=1
print("{} {:.2f}".format(os.getcwd().split('/')[-1], count))
