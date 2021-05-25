#!/bin/bash

mkdir -p ./output
echo 'language | python' > ./output/evaluation.txt

if [ -z "$1" ];
then
  echo "Version | dev" >> ./output/evaluation.txt
else
  echo "Version | $1" >> ./output/evaluation.txt
fi

python training.py mortality
python training.py fss
python testing.py $1
R CMD BATCH --vanilla "--args $1" evaluate.R output/evaluate.Rout
