#!/bin/bash

input=input.txt

# col 1
list1=()
# col 2
list2=()

while IFS= read -r line || [ -n "$line" ]; do 
	# grab everything before the triple space
    num1=${line%%   *}
	# grab everything after the triple space 
	num2=${line##*   }
	# removing leading / trailing whitespace from nums2 (idk why its there lol)
	num2=$(echo "$num2" | xargs)

	list1+=( "$num1" )
	list2+=( "$num2" )

done < "$input" 

# new dictionary called values 
declare -A values

arrLength=${#list1[@]}

ans=0
for (( i=0; i<${arrLength}; i++ ));
do
	# if in dictionary, use the dict value
	if [[ -v values["${list1[$i]}"] ]]; then
		simScore=${values[${list1[$i]}]}
	# if not, then count # of times its in list2 and save in dict
	else
		count=$(grep -o ${list1[$i]} <<< ${list2[*]} | wc -l)
		simScore=$(( $count * ${list1[$i]} ))

		values[${list1[$i]}]=$simScore
	fi

	ans=$(($ans + $simScore))
done

echo $ans