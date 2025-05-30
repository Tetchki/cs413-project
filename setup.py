import os
import subprocess
import sys
import urllib.request

"""
def setup_deepLSD_weights():
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
"""

def download_file(url, dest_path):
    if not os.path.isfile(dest_path):
        print(f"Downloading {os.path.basename(dest_path)}...")
        urllib.request.urlretrieve(url, dest_path)
    else:
        print(f"{os.path.basename(dest_path)} already exists, skipping download.")

def setup_deepLSD_weights():
    """Create the weights directory in ext/DeepLSD and download the necessary files if not already present."""
    deep_lsd_dir = 'ext/DeepLSD'
    if os.path.isdir(deep_lsd_dir):
        weights_dir = os.path.join(deep_lsd_dir, 'weights')
        os.makedirs(weights_dir, exist_ok=True)

        wireframe_file = os.path.join(weights_dir, 'deeplsd_wireframe.tar')
        md_file = os.path.join(weights_dir, 'deeplsd_md.tar')

        download_file('https://cvg-data.inf.ethz.ch/DeepLSD/deeplsd_wireframe.tar', wireframe_file)
        download_file('https://cvg-data.inf.ethz.ch/DeepLSD/deeplsd_md.tar', md_file)
    else:
        print("DeepLSD directory not found!")

from setuptools import setup, find_packages

setup(name='cs413-project', version="0.0", packages=find_packages())

# Install requirements

#Setup DeepLSD
print("Setting up DeepLSD...")

# Setup DeepLSD weights
setup_deepLSD_weights()