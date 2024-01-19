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
binding_res=[len(pep1)+41,len(pep1)+42,len(pep1)+43]

pep1_pair=[]
for i in range(len(pep1)):
    for j in binding_res:    
         pep1_pair.append([j,i])

#print(pep1_pair)

pep2_pair=[]
for i in range(len(prot)+len(pep1),len(whole)-2):
    for j in binding_res: 
        pep2_pair.append([j,i])


f=open('count.dat','w')

all_pep=sorted(glob.glob('Seq*/'))
sorted_pep = sorted(all_pep, key=lambda x: int(x[3:-1]))
print(sorted_pep)
for i in sorted_pep:
    for j in sorted_pep:
        all_pdb = glob.glob(i+j+'complex*/*.pdb')
        pep1_dist=[]
        pep2_dist=[]
        #print(all_pdb)
        for k in all_pdb:
            a=md.load(k)
            dist = md.compute_contacts(a, pep1_pair, scheme='CA')[0]
            pep1_dist.append(np.mean(dist))
        for k in all_pdb:
            a=md.load(k)
            dist = md.compute_contacts(a, pep2_pair, scheme='CA')[0]
            pep2_dist.append(np.mean(dist))
        #print(pep1_dist,pep2_dist)
        count=0
        for p1,p2 in zip(pep1_dist, pep2_dist):
            if p1 > p2:
                count+=1
        print(j, 'done') 
        f.write("{} {} {:.2f}\n".format(i[:-1],j[:-1], count))

