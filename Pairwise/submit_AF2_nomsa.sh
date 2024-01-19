#!/bin/bash
#SBATCH --job-name=AF2
#SBATCH --output=AF2.out
#SBATCH --error=AF2.err
#SBATCH --mail-type=ALL
##SBATCH --mail-user=arup.mondal@ufl.edu
#SBATCH --time=2:00:00
#SBATCH --ntasks=1
#SBATCH --distribution=cyclic:cyclic
#SBATCH --mem-per-cpu=30000
#SBATCH --account=alberto.perezant
#SBATCH --cpus-per-gpu=1
#SBATCH --gpus-per-task=1
#SBATCH --partition=gpu
#SBATCH --constraint=a100



module load cuda/11.1.0
export LD_LIBRARY_PATH=/blue/alberto.perezant/arup.mondal/Source/AlphaFold/localcolabfold/colabfold_batch/colabfold-conda/lib

colabfold_batch complex.a3m --model-type alphafold2_ptm complex
colabfold_batch complex.a3m --model-type alphafold2_ptm complex_2
