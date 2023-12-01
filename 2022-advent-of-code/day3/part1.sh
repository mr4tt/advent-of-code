#!/bin/bash

#input=input3.txt
input=test.txt

score=0

while IFS= read -r line; do
	length=${#line}
	rucksack=$((length / 2))
	# rucksack=$(({#line}  / 2)) note to self figure out how to do in one line
	declare -a rucksack1
	declare -a rucksack2

	# setting hashmaps for letters1 and letters 2
	declare -A letters1
	declare -A letters2

	# trying to put first half of letters into first hashmap
	for ((i=0; i<${#rucksack}; i++)); do
		if [ -v letters1["${line:$i:1}"] ]; then
			((letters1["${line:$i:1}"]++))
		else
			letters1["${line:$i:1}"]=1
		fi 
	done
#	for ((i=; i<${#rucksack}; i++)); do rucksack1[$i]="${line:$i:1}"; done

	#declare -p rucksack1

	echo "${!letters1[@]}"	


#	rucksack1=${line:0:$rucksack}
#	rucksack2=${line:$rucksack}
#
#	#echo $rucksack1
#	#echo $rucksack2
#
#	
#
#	printf "%d\n" "'$repeated"


done < "$input" && echo $score

