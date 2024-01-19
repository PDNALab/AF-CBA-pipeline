#!/bin/bash
while read a b
do
        echo $a $b
	cp complex.a3m $a
	cp selected_seq.txt $a
	cp setup.sh $a
	cd $a/
      	sed -i 's/%/'$b'/g' complex.a3m
	cd ../

#exit
done < random_sequences.txt

