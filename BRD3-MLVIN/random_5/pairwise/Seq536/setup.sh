#!/bin/bash
while read a b
do
        echo $a $b
        mkdir $a
	cp complex.a3m $a
	cd $a/
      	sed -i 's/@/'$b'/g' complex.a3m
	cd ../



cd  $a
sbatch ../../submit_AF2_nomsa.sh
cd ../

#exit
done < selected_seq.txt
echo "competitive binding job submitted."

