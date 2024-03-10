from Bio.PDB import PDBParser
import numpy as np
import prody
from matplotlib import pyplot as plt
import glob

def longest_consecutive_greater(numbers, threshold):
    max_consecutive = []
    current_consecutive = []

    for num in numbers:
        if num > threshold:
            current_consecutive.append(num)
            if len(current_consecutive) > len(max_consecutive):
                max_consecutive = current_consecutive.copy()
        else:
            current_consecutive = []

    return max_consecutive


total_frag=glob.glob('Seq*.pdb')

# Define the key residues and their corresponding atom names
key_residues = {
    "I42": "CA",
    "E43": "CA",
    "I44": "CA",
}

# Define the output file
plddt_list=[]
distance_list=[]
#output_file = "distances_plddt.txt"
#output_file_sel = "distances_plddt_selected.txt"
f=open('distances_plddt.txt', "w")
f1=open('distances_plddt_selected.txt', "w")
# Loop through PDB files from Seq1.pdb to Seq1901.pdb
#for seq_num in range(1, len(total_frag)+1):  # Adjust the range as needed
#    pdb_file = f"Seq{seq_num}.pdb"
for pdb_file in total_frag:   
    try:
        # Initialize a list to store distances for each PDB file
        distances = []

        # Load the PDB file
        parser = PDBParser()
        structure = parser.get_structure("protein", pdb_file)

        # Extract the peptide (chain A) and protein (chain B) residues
        peptide_residues = []
        protein_residues = []

        for model in structure:
            for chain in model:
                if chain.get_id() == "A":
                    peptide_residues.extend(chain)
                elif chain.get_id() == "B":
                    protein_residues.extend(chain)

        # Calculate distances for each key residue to all peptide residues
        for key_residue, atom_name in key_residues.items():
            key_residue_atoms = [residue[atom_name] for residue in protein_residues if residue.get_id()[1] == int(key_residue[1:])]
            for atom in key_residue_atoms:
                for peptide_residue in peptide_residues:
                    if atom_name in peptide_residue:
                        distance = atom - peptide_residue[atom_name]
                        distances.append(distance)

        # Calculate the average distance
        if distances:
            average_distance = np.mean(distances)
        else:
            average_distance = "N/A"
        
        # Calculate pLDDT
        peptide_ca=prody.parsePDB(pdb_file,chain='A',subset='CA')
        result=longest_consecutive_greater(peptide_ca.getBetas(), 70.0)
        print(result)
        if len(result)>=6:
            pep_plddt=np.mean(result)
        else:
            pep_plddt=np.mean(peptide_ca.getBetas()) 
        plddt_list.append(pep_plddt)
        distance_list.append(average_distance)
        # Append the result to the output file
        #with open(output_file, "a") as f:
        f.write(f"{pdb_file[:-4]} {average_distance} {pep_plddt}\n")
        #with open(output_file_sel, "a") as f:
        pep_seq= peptide_ca.getSequence()
        if pep_plddt>=70 and average_distance <20:
            f1.write(f"{pdb_file[:-4]} {pep_seq}\n")
        #if pep_seq==open('pep.dat').readlines()[0][:-1]:
         #   print(pep_seq)
          #  pep_d=average_distance
           # pep_p=pep_plddt
            
    except FileNotFoundError:
        # Handle absent PDB files
        #with open(output_file, "a") as f:
        f.write(f"{pdb_file}: PDB not found\n")
    except Exception as e:
        # Handle other exceptions
        #with open(output_file, "a") as f:
        f.write(f"{pdb_file}: Error - {str(e)}\n")
f.close()
f1.close()
#print(pep_d,pep_p)
print(len(distance_list))
print(len(plddt_list))
colors = ['#B40426' if i < 20 and j>=  70 else '#3B4CC0' for i, j in zip(distance_list,plddt_list)]
print(len(colors))
plt.scatter(distance_list,plddt_list,c=colors,alpha=0.5)
#plt.scatter(pep_d,pep_p,c='#0AB2BA',marker='*',s=200, zorder=3,edgecolors='black')
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.savefig('binding.pdf')
