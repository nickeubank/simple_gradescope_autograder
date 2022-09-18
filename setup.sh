#!/usr/bin/env bash

# install conda
wget -nv -O /autograder/source/miniconda_install.sh "https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh"
chmod +x /autograder/source/miniconda_install.sh
/autograder/source/miniconda_install.sh -b
echo "export PATH=/root/miniconda3/bin:\$PATH" >> /root/.bashrc

export PATH=/root/miniconda3/bin:$PATH

# install dependencies with conda and mamba
# (Mamba is parallelized conda.)
conda install mamba -n base -c conda-forge
mamba env create -f /autograder/source/environment.yml

# setup conda shell
# to enable environments.
conda init --all

# Add little helper utility not in pip
# that generates a result json from 
# pytest output.

# conda init only works after restarting
# session, so have to directly run here
# so can turn on grader env.
source /root/miniconda3/etc/profile.d/conda.sh
conda activate grader

cd /autograder/source/
git clone https://github.com/nickeubank/pytest_utils.git
cd pytest_utils
pip install -e .
