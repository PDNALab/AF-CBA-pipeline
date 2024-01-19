Step0.Installation of ColabFold:

Install the local version of ColabFold, localcolabfold from (https://github.com/YoshitakaMo/localcolabfold) as follows:
module load cuda/11.1.0
module load gcc/9.3.0
wget https://raw.githubusercontent.com/YoshitakaMo/localcolabfold/main/install_colabbatch_linux.sh
bash install_colabbatch_linux.sh

Step1. Fragment library generation.

Save the full length interacting protein sequence as full_length.dat and run Library_generation/sequence_generation.py script. We need to use an appropriate peptide length that we want to fragment into. In the given script we used 25 as the peptide length. This will generate output_sequences.txt file with all the fragment sequence and seqeunce ID.

Step2. AF2 binding of all fragment.

Copy output_sequences.txt file file to a new directory. Run AF_binding/setup_first.sh that will setup directories for running AF calculations. Then execute AF_binding/submit_first.sh to submit all AF jobs. We need to use appropriate receptor sequence in AF_binding/setup_first.sh script and submit_AF2_ptm.sh script should be changed accordinly. 

Once all jobs are finished, run AF_binding/top_1.sh to copy all top1 model to a directory and then run AF_binding/distance.py if we know the native, else AF_binding/distance_nonative.py if we do not know the native binder. (The later is jsut to highlight the native epitope in the plot)

distances_plddt_selected.txt will have the selected peptides for the next round.

Step3. Random 5 competition.

Create a new directory. 
Copy distances_plddt_selected.txt to selected_seq.txt. 
Choose 5 random sequences from the selected pool. 
Create random_sequences.txt with the random 5 sequences and their Seq ID. 
Copy the files from Random_5 folder. 
Execute random_setup.sh to setup all the working directories.
Execute setup.sh in each of the 5 directories corresponding to the 5 random sequences. This will submit all the jobs.

All these steps can be performed by executing Random_5/random_5.sh (May need some changes depending on directory organization)

Here we need complex.a3m which is given for a BRD3 system, howover it can be created by running an AF competitive with MSAs and then deleting the peptide MSAs from the a3m file as we do not use peptide MSA for AF-CBA. 

Once the jobs are done, we can run Random_5/score_random.sh to score each selected peptides against each of the 5 random peptides. This will generate score_shortlisted.dat file. We only keep the sequences uptop score 8.00 as they convincingly outcompete the references (i.e. random selected peptides). We then use Random_5/get_common.py to get the peptide fragments that outcompete all these 5 random fragments.

For plotting the result, we can use Random_5/plot_random.py after executing Random_5/add_ref.sh to add a dummy values for the self competition. This step need Random_5/base.fasta to read peptides and receptor lengths. 

Executing Random_5/get_common.py file will generate selected_for_pw.dat file will have all the sequences that are selected for the final pairwise competition stage.

Step4. All-by-all pairwise competition

Create  a new directory
Copy selected_for_pw.dat with their associated sequences to the new directory as selected_seq.txt
Create directories for all selected peptides
Copy selected_seq.txt to random_sequences.txt 
Copy all the files from Pairwise directory
Execute random_setup.sh to setup all the working directories.
Execute setup.sh in each of the directories corresponding to each of the selected sequences. This will submit all the jobs.

All these steps can be executed by executing Pairwise/pairwise.sh. (May need some changes depending on directory organization)

Once all jobs are done, execute Pairwise/count.py to score them and generate count.dat with the score. Then execute plot.py to plot the results. Looking at the column, we can identify the best binder. The darker the red, the higher the outcompeting confidence. Ideally the for the best binder, we would have all red in the column and all blue in the row. 

