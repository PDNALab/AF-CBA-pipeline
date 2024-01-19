#!/bin/bash

## here I have taken only the trail_1 structures

mkdir top_1/
while read a b
do
	cp $a/complex/seq_unrelaxed_rank_001_*.pdb top_1/$a.pdb

	#exit
	
done < output_sequences.txt
