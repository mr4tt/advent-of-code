#!/bin/bash

input=input2.txt
score=0

while IFS= read -r line; do

	if [ ${line:2:1} = "Y" ]; then
		score=$((score+3))
	elif [ ${line:2:1} = "Z" ]; then
		score=$((score+6))
	fi

	if [ "$line" = "A Y" ] || [ "$line" = "B X" ] || [ "$line" = "C Z" ]; then
		((score++))
	elif [ "$line" = "A Z" ] || [ "$line" = "B Y" ] || [ "$line" = "C X" ]; then
		score=$((score+2))
	else
		score=$((score+3))
	fi
	echo $score
done < "$input" && echo $score
 


