#! /bin/bash

#---------------------------------------
# $Author: ee364f07 $
# $Date: 2017-01-18 14:38:10 -0500 (Wed, 18 Jan 2017) $
#---------------------------------------

# Do not modify above this line.

#input validation
if (( $# != 2 )) 
then
	echo "Usage: collect_stats.bash <file> <sport>"
	exit 1
fi

#check if file exists
if [[ ! -e $1 ]]
then
	echo "error: $1 does not exist"
	exit 2
fi

Filename=$1
Sportsearch=$2
totathletes=0
totmedals=0
winmedals=0

#read file line by line
while read line
do
	sport=$(echo $line | cut -f2 -d',')
	numMedals=$(echo $line | cut -f3 -d',')
	athlete=$(echo $line | cut -f1 -d',')

	if [[ $sport == $Sportsearch ]]
	then
		let totathletes=totathletes+1
		let totmedals=totmedals+numMedals

		if (( $numMedals > $winmedals ))
		then
			winmedals=$numMedals
			winathlete=$athlete
		fi
	fi


done < $1

echo "Total athletes: $totathletes"
echo "Total medals won: $totmedals"
echo "$winathlete won the most medals: $winmedals"

exit
