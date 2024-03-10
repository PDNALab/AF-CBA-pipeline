#!/bin/bash
while read a b 
do
        echo $a
        cd $a
	sbatch ../../../upload/AF_binding/submit_AF2_ptm.sh
	cd ../

#exit
done < output_sequences.txt
echo "job submitted"

