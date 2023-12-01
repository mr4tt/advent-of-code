#!/bin/bash

input=input2.txt

# A = opp plays rock
# B = paper
# C = scissors

# X = you play rock
# Y = paper
# Z = scissors

score=0

while IFS= read -r line; do
	if [ "$line" = "A Y" ] || [ "$line" = "B Z" ] || [ "$line" = "C X" ]; then
		score=$((score+6))
	elif [ "$line" = "A X" ] || [ "$line" = "B Y" ] || [ "$line" = "C Z" ]; then
		score=$((score+3))
	fi

	if [ ${line:2:1} = "X" ]; then
		((score++))
	elif [ ${line:2:1} = "Y" ]; then
		score=$((score+2))
	elif [ ${line:2:1} = "Z" ]; then
		score=$((score+3))
	fi
done < "$input" && echo $score
 


