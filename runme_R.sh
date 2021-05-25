#!/bin/bash

mkdir -p output
echo "language | r" > ./output/evaluation.txt

if [ -z "$1" ];
then
  echo "Version | dev" >> ./output/evaluation.txt
else
  echo "Version | $1" >> ./output/evaluation.txt
fi

R CMD BATCH --vanilla '--args mortality' training.R output/training_mortality.Rout
R CMD BATCH --vanilla '--args fss'       training.R output/training_fss.Rout
R CMD BATCH --vanilla "--args $1" testing.R output/testing.Rout
R CMD BATCH --vanilla "--args $1" evaluate.R output/evaluate.Rout
