for i in Seq*; do cd $i; cp score.dat score_added_ref.dat; sed -i "1 a\\${i} 100" score_added_ref.dat; cd ..; done
