#!/bin/bash

input=input.txt
# input=test.txt

elf=1
greatestElf=1
sum=0
greatestSum=0

while IFS= read -r line; do
# 	echo $line
	if [ -n "$line" ]; then
		sum=$((sum+line))
	else
		if [ $sum -gt $greatestSum ]; then
			greatestSum=$sum
			greatestElf=$elf
		fi
		if [ $elf == 11 ]; then
			echo $sum
		fi
		((elf++))
# 		echo $elf
		sum=0
	fi
  
done < "$input" && echo $greatestElf

