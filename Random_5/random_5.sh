cp ../binding/top_1/distances_plddt_selected.txt selected_seq.txt
shuf -n 5 selected_seq.txt | awk '{print $1}' | xargs mkdir
for i in Seq*; do grep "${i} " selected_seq.txt >>random_sequences.txt; done
cp ../../Random_5/* .
bash random_setup.sh 
for i in Seq*; do cd $i;  bash setup.sh ;  cd ..;  done
