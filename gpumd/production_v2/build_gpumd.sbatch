#!/bin/bash
#SBATCH -J gpumd_build
#SBATCH -M notchpeak
#SBATCH -p notchpeak-guest
#SBATCH -A owner-guest
#SBATCH -N 1 -n 16
#SBATCH -t 01:00:00
#SBATCH -o /uufs/chpc.utah.edu/common/home/u1496771/mat_theory/gpumd_v2/build_%j.txt
set -x
module purge; module load cuda/12.8.1
cd ~/mat_theory/gpumd_v2/GPUMD/src
sed -i 's/-std=c++14/-std=c++17/' makefile main_replica/makefile
ARCH="-gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -gencode arch=compute_86,code=sm_86 -gencode arch=compute_89,code=sm_89 -gencode arch=compute_90,code=sm_90 -gencode arch=compute_120,code=sm_120 -gencode arch=compute_90,code=compute_90"
make clean >/dev/null 2>&1
make -j16 gpumd CUDA_ARCH="$ARCH"
ls -la gpumd && echo BUILD_OK
