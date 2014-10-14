#!/bin/bash
## xander make wrapper to be used with MSU hpc.
## qsub -l walltime=hh:mm:ss,mem=60000mb -v targets=all,workdir=`pwd` path/to/make_wrapper.sh 

module load HMMER/3.0
module load bowtie/2.2.1
module load CDHIT/4.6.1b
module load SAMTools/0.1.12a
module load Python
module load NumPy/1.6.1
module load matplotlib
module load Scipy/0.0.0

cd $workdir
make $targets
