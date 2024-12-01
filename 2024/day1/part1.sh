# #!/bin/bash

input=input.txt

list1=()
list2=()

while IFS= read -r line || [ -n "$line" ]; do 
    num1=${line%%   *}
	num2=${line##*   }
	# removing leading / trailing whitespace from nums2:
	num2=$(echo "$num2" | xargs)

	list1+=( "$num1" )
	list2+=( "$num2" )

done < "$input" 

# sort the lists 
IFS=$'\n' list1=($(sort <<<"${list1[*]}"))
IFS=$'\n' list2=($(sort <<<"${list2[*]}"))
unset IFS

arrLength=${#list1[@]}

ans=0
for (( i=0; i<${arrLength}; i++ ));
do
	# subtract each value from each other 
	temp=$((${list1[$i]}-${list2[$i]}))
	# remove the negative sign, if any
	ans=$(($ans + ${temp#-}))
done

echo $ans