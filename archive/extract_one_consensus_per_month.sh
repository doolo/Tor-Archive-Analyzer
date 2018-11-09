#!/bin/bash

if [ -d per_month_consensuses ]; then
   mkdir per_month_consensuses
fi

for year in {07..18}; do
    for month in {01..12}; do
        echo "${year}-${month}"
        tar -xvf "consensuses/consensuses-20${year}-${month}.tar.xz" "consensuses-20${year}-${month}/15/20${year}-${month}-15-00-00-00-consensus"
        mv "consensuses-20${year}-${month}" per_month_consensuses
    done
done
