from matplotlib import pyplot as plt
import numpy as np
import glob
from mpl_toolkits.axes_grid1 import make_axes_locatable

def increment_numerical_part(element):
    numerical_part = element[3:]
    incremented_numerical_part = str(int(numerical_part) + 1)
    result = 'Seq' + incremented_numerical_part
    return result

all_score=glob.glob('Seq*/score_added_ref.dat')
sorted_score = sorted(all_score, key=lambda x: int(x.split('/')[0][3:]))

l1=np.loadtxt(sorted_score[0],dtype=str).tolist()
l1.sort(key=lambda x: int(x[0][3:]))
xticks=np.array(l1)[:,0]
x_label=list(xticks)
#x_label=[increment_numerical_part(element) for element in x_labels]


def ger_sorted_score(i):
    l1=np.loadtxt(sorted_score[i],dtype=str).tolist()
    l1.sort(key=lambda x: int(x[0][3:]))
    a1=np.array(l1)[:,1]
    a1_flt=a1.astype(np.float)
    a1_per=a1_flt/10.
    aa= np.where(a1_per<0.5, a1_per-1, a1_per)
    aa1= np.where(aa==10.0, 0.0, aa)
    return aa1

ref0=ger_sorted_score(0)
ref1=ger_sorted_score(1)
ref2=ger_sorted_score(2)
ref3=ger_sorted_score(3)
ref4=ger_sorted_score(4)
print(len(ref0),len(ref1),len(ref2),len(ref3),len(ref4))
x=np.arange(1, len(l1)+1)
y=np.ones(len(l1))

plt.figure(figsize=(18,3))
plt.scatter(x,y,c=ref0,cmap='coolwarm',marker='o',s=100,alpha=0.7,vmin=-1, vmax=1,edgecolors='white')
plt.scatter(x,y+1,c=ref1,cmap='coolwarm',marker='o',s=100,alpha=0.7,vmin=-1, vmax=1,edgecolors='white')
plt.scatter(x,y+2,c=ref2,cmap='coolwarm',marker='o',s=100,alpha=0.7,vmin=-1, vmax=1,edgecolors='white')
plt.scatter(x,y+3,c=ref3,cmap='coolwarm',marker='o',s=100,alpha=0.7,vmin=-1, vmax=1,edgecolors='white')
plt.scatter(x,y+4,c=ref4,cmap='coolwarm',marker='o',s=100,alpha=0.7,vmin=-1, vmax=1,edgecolors='white')


y_ticks = [1,2,3,4,5]
y_label=[i.split('/')[0] for i in sorted_score]
#y_label=[increment_numerical_part(element) for element in y_labels]

plt.xticks(x, x_label, rotation=90)
plt.yticks(y_ticks, y_label)

plt.xticks(fontsize=12)
plt.yticks(fontsize=14)
plt.xlim(0,len(x)+1)

divider = make_axes_locatable(plt.gca())
cax = divider.append_axes("right", size="1%", pad=0.1)
colorbar=plt.colorbar(shrink=0.83,cax=cax)
colorbar.ax.tick_params(labelsize=11)
plt.tight_layout()

plt.savefig('random_5.pdf')
plt.show()

