#!/bin/bash
while read a b
do
        echo $a $b
        mkdir $a
        echo ">seq"  > ./$a/"complex.fasta"
	echo "$b:SYDEKRQLSLDINRLPGEKLGRVVHIIQSREPSLRDSNPDEIEIDFETLKPTTLRELERYVKSCLQKK" >> ./$a/"complex.fasta"   #change the receptor sequence depending on the system

	# Create a colabfold AF run script
	# Create a colabfold AF run script
#exit
done < output_sequences.txt
echo "FASTA files have been created and base.fasta has been updated."

