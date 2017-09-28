#! /bin/bash

#check input for only 1 parameter
if (( $# != 1 ))
then 
	echo "Usage: line_num.bash <filename>";
	exit
fi

#check if file is readable
if [[ ! -r $1 ]]
then
	echo "Error. File is not readable"
fi

cnt=1
while read file_line
do
	echo "$cnt: $file_line"
	let cnt=cnt+1
done < $1


exit
