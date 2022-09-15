#!/usr/bin/env bash

# install conda
wget -nv -O /autograder/source/miniconda_install.sh "https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh"
chmod +x /autograder/source/miniconda_install.sh
/autograder/source/miniconda_install.sh -b
echo "export PATH=/root/miniconda3/bin:\$PATH" >> /root/.bashrc

export PATH=/root/miniconda3/bin:$PATH

# install dependencies with conda
conda install mamba -n base -c conda-forge
mamba env create -f /autograder/source/environment.yml

# conda env create -f /autograder/source/environment.yml

# set conda shell
conda init --all

# Add little helper
source /root/miniconda3/etc/profile.d/conda.sh
conda activate grader
cd /autograder/source/
git clone https://github.com/ucsb-gradescope-tools/pytest_utils.git
cd pytest_utils
pip install -e .
