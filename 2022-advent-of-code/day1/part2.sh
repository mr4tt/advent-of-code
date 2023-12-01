#!/bin/bash

input=input.txt
# input=test.txt

declare {sum,firstSum,secondSum,thirdSum}=0

while IFS= read -r line; do	
# 	echo $line
	if [ -n "$line" ]; then
		sum=$((sum+line))
	else
		if [ "$sum" -gt "$firstSum" ]; then
			thirdSum=$secondSum
			secondSum=$firstSum

			firstSum=$sum
		elif [ "$sum" -gt "$secondSum" ]; then
			thirdSum=$secondSum

			secondSum=$sum
		elif [ "$sum" -gt "$thirdSum" ]; then
			thirdSum=$sum
		fi
		sum=0
	fi
 
done < "$input" && echo "$firstSum" + "$secondSum" + "$thirdSum"

#done < "$input" && echo $((firstSum+secondSum+thirdSum))

echo $((firstSum+secondSum+thirdSum))


