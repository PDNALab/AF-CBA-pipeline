mkdir pairwise
awk 'NR==FNR { data[$1] = $2; next } $1 in data { $2 = data[$1] } 1' selected_seq.txt selected_for_pw.dat > pairwise/selected_seq.txt
cd pairwise
shuf  selected_seq.txt | awk '{print $1}' | xargs mkdir
cp selected_seq.txt random_sequences.txt
cp ../../../upload/Pairwise/* .
bash random_setup.sh 
for i in Seq*; do cd $i;  bash setup.sh ;  cd ..;  done
