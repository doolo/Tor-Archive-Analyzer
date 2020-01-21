#!/bin/bash

if [ -d per_month_consensuses ]; then
   mkdir per_month_consensuses
fi

for year in {07..18}; do
    for month in {01..12}; do
	for day in {01..31}; do
            echo "${year}-${month}"
            tar -xvf "consensuses/consensuses-20${year}-${month}.tar.xz" "consensuses-20${year}-${month}/${day}/20${year}-${month}-${day}-00-00-00-consensus" &
	done
	wait
	mv "consensuses-20${year}-${month}" per_month_consensuses
    done
done
