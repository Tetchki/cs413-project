import os
import subprocess
import sys

def install_requirements_from_top_level_submodules():
    """Install requirements from top-level requirements.txt in each submodule of ext/."""
    ext_dir = 'ext'

    for submodule in os.listdir(ext_dir):
        submodule_path = os.path.join(ext_dir, submodule)
        # Only consider directories and ensure they have a requirements.txt file
        if os.path.isdir(submodule_path) and 'requirements.txt' in os.listdir(submodule_path):
            req_file = os.path.join(submodule_path, 'requirements.txt')
            print(f"Installing from {req_file}...")
            subprocess.check_call([os.sys.executable, "-m", "pip", "install", "-r", req_file])


def setup_deepLSD_weights():
    """Create the weights directory in ext/DeepLSD and download the necessary files if not already present."""
    deep_lsd_dir = 'ext/DeepLSD'
    if os.path.isdir(deep_lsd_dir):
        weights_dir = os.path.join(deep_lsd_dir, 'weights')
        os.makedirs(weights_dir, exist_ok=True)

        # Check if the weight files already exist
        wireframe_file = os.path.join(weights_dir, 'deeplsd_wireframe.tar')
        md_file = os.path.join(weights_dir, 'deeplsd_md.tar')

        if not os.path.isfile(wireframe_file):
            print("Downloading deeplsd_wireframe.tar...")
            subprocess.check_call(
                ['wget', 'https://cvg-data.inf.ethz.ch/DeepLSD/deeplsd_wireframe.tar', '-O', wireframe_file])
        else:
            print("deeplsd_wireframe.tar already exists, skipping download.")

        if not os.path.isfile(md_file):
            print("Downloading deeplsd_md.tar...")
            subprocess.check_call(['wget', 'https://cvg-data.inf.ethz.ch/DeepLSD/deeplsd_md.tar', '-O', md_file])
        else:
            print("deeplsd_md.tar already exists, skipping download.")
    else:
        print("DeepLSD directory not found!")


from setuptools import setup, find_packages

setup(name='cs413-project', version="0.0", packages=find_packages())

# Install requirements
install_requirements_from_top_level_submodules()

#Setup DeepLSD
print("Setting up DeepLSD...")

# Setup DeepLSD weights
setup_deepLSD_weights()

# Setup pyprogressivex
print("Setting up pyprogressivex...")
#run pip3 install -e ext/progressive-x
subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "ext/progressive-x"])

# Setup pyprogressivex
print("Setting up SSIS...")
#python setup.py build develop in ext/SSIS
subprocess.check_call([sys.executable, "setup.py", "build", "develop"], cwd="ext/SSIS")
