for file in a b c d e f
do
	
cat ${file}.txt | ./main > ${file}.out

done

