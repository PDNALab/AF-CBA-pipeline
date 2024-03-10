import numpy as np
import glob
all_score=glob.glob('Seq*/score_shortlisted.dat')
l1=np.loadtxt(all_score[0],dtype=str)[:,0]
l2=np.loadtxt(all_score[1],dtype=str)[:,0]
l3=np.loadtxt(all_score[2],dtype=str)[:,0]
l4=np.loadtxt(all_score[3],dtype=str)[:,0]
l5=np.loadtxt(all_score[4],dtype=str)[:,0]


s1=set(l1)
s2=set(l2)
s3=set(l3)
s4=set(l4)
s5=set(l5)

inter=s1.intersection(s2).intersection(s3).intersection(s4).intersection(s5)
inter_list=list(inter)
f=open('selected_for_pw.dat','w')
for i in inter_list:
    f.write('{}\n'.format(i))
f.close()

