import os
import urllib.request

def download_file(url, dest_path):
    if not os.path.isfile(dest_path):
        print(f"Downloading {os.path.basename(dest_path)}...")
        urllib.request.urlretrieve(url, dest_path)
    else:
        print(f"{os.path.basename(dest_path)} already exists, skipping download.")

def setup_deepLSD_weights():
    """Creates the weights directory in ext/DeepLSD and downloads the necessary files if not already present."""
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

if __name__ == "__main__":
    print("Setting up DeepLSD...")
    setup_deepLSD_weights()