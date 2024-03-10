import os
import glob
import numpy as np
import mdtraj as md

whole=open('base.fasta').readlines()[-1].strip()
colon=[]
for i in range(len(whole)):
    if whole[i]==':':
        colon.append(i)

pep1=whole[:colon[0]]
prot=whole[colon[0]+1:colon[1]]
pep2=whole[colon[1]+1:]
key_res=[41,42,43]


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


f=open('count.dat','w')

all_pep=sorted(glob.glob('Seq*/'))
sorted_pep = sorted(all_pep, key=lambda x: int(x[3:-1]))
print(sorted_pep)
for i in sorted_pep:
    for j in sorted_pep:
        all_pdb = glob.glob(i+j+'complex*/*.pdb')
        pep1_dist=[]
        pep2_dist=[]
        for k in all_pdb:
            dist1=ref(key_res,pep1,k)
            dist2=comp(key_res,pep2,k)
            pep1_dist.append(dist1)
            pep2_dist.append(dist2)
        count=0
        for p1,p2 in zip(pep1_dist, pep2_dist):
            if p1 > p2:
                count+=1
        print(j, 'done') 
        f.write("{} {} {:.2f}\n".format(i[:-1],j[:-1], count))

