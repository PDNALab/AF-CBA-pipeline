for i in Seq*; do cd $i; bash all.sh >score.dat; sort -k 2 -r -n score.dat >score_sorted.dat; cp score_sorted.dat score_shortlisted.dat; cd ..; done
