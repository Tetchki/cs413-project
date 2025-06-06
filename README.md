# CS413 Project: Estimating Manhattan frames to analyze structural inconsistencies

We use vanishing points and camera intrinsics to extract the dominant manhattan frame in an image to test the orthogonality constraints expected from real-world architectures. This method obtained an F1-Score of 0.75 on a mixed real/generated images handmade benchmark. This method showed signs of robustness to resampling, a common weakness of classical learning-based detectors, although more work is needed to explore it.
## 🛠 Installation

> **Tested with:**
> * **Ubuntu** 24.04
> * **Python** 3.12
> * **CUDA** 12.6

Clone the repository and set up the environment:

```bash
git clone --recurse-submodules git@github.com:Tetchki/cs413-project.git
cd cs413-project
```
1. **Create a Python 3.12 virtual environment**

2. **Install pip-tools**

    This project uses [`pip-tools`](https://github.com/jazzband/pip-tools) to manage dependencies in a reproducible way.
   ```bash
   pip install pip-tools
   ```
3. **Compile requirements.txt from requirements.in**
   
    Resolves all dependencies from `requirements.in` into a fully pinned `requirements.txt`.
    
    *Note: This may take a while.*
   ```bash
   pip-compile --verbose requirements.in
   ```
4. **Install dependencies**

   Install all dependencies and their exact versions as specified in `requirements.txt`.

    *Note: This may take a while.*
   ```bash
   pip install -r requirements.txt
   ```
   
5. **Install the DeepLSD submodule**

   Some code in this project requires pre-trained weights for DeepLSD. Download them with:

   ```bash
   python3 download_deeplsd_weights.py
   ```

### 🧱 Manual Setup for DeepLSD Weights (Optional)

If you prefer to download the weights manually instead of using `python3 download_deeplsd_weights.py`, follow these steps:

1. **Ensure the DeepLSD submodule is initialized:**

   * Confirm that the folder `ext/DeepLSD` exists. If it doesn’t, run:

     ```bash
     git submodule update --init --recursive
     ```

2. **Create the weights folder:**

   * Inside the `ext/DeepLSD` directory, create a subfolder named `weights`.
   * The folder structure should look like this:

     ```
     ext/
       └── DeepLSD/
           └── weights/
           └── ...
     ```

3. **Download the required model files:**

   * [deeplsd\_wireframe.tar](https://cvg-data.inf.ethz.ch/DeepLSD/deeplsd_wireframe.tar)
   * [deeplsd\_md.tar](https://cvg-data.inf.ethz.ch/DeepLSD/deeplsd_md.tar)

4. **Move the downloaded files into the `weights/` folder:**

   * Place both `.tar` files into `ext/DeepLSD/weights/`.

---

## Running the Demo

The demo is provided in the Jupyter notebook called **`playground.ipynb`**. It runs on two example images located in the **`data/`** folder.

To run the demo:

1. Open `playground.ipynb` in Jupyter.
2. Run the cells sequentially to execute the full pipeline on the sample images.

You can pass `verbose=True` to the main pipeline function if you want to see intermediate results and detailed information about each processing step.

Make sure all dependencies are installed and the `data/` folder contains the required images before running the notebook.

---

## 📁 Data

* The `data/` directory contains the datasets used for finetuning and evaluation.
* You can download the full data folder from [here](https://drive.google.com/drive/folders/1KE5jK0FZSqztiJwzxzEN0hkqLp3hMu_C?usp=sharing).
* The `data/synthbuster/keep` folder contains the 100 hand-picked building examples from the Synthbuster dataset that fit our scene geometry assumptions. If you want you can download the full Synthbuster dataset from [here](https://zenodo.org/records/10066460). Put its content inside the `data/synthbuster/` folder.
* Use the `extract_dataset.ipynb` notebook to hand-pick building examples from the Synthbuster dataset that fit our scene geometry assumptions.

## 📷 Camera Calibration Experiments

* Use `intrinsics_experiments.ipynb` to compare the performance of GeoCalib and Perspective Field methods for camera intrinsics estimation.

## 🚀 Benchmark Pipeline

* `pipeline.ipynb` is the main notebook to run the full geometry-based detection pipeline and generate benchmark results.

## 🧪 Playground Demo

* `playground.ipynb` provides a minimal demo to test the system on one real and one generated image for quick validation.

## 📌 Notes

* This project assumes a focus on geometric priors like vanishing points, line segment distributions, and camera intrinsics to identify generated images.
* The DeepLSD and Geolib submodules are required for full functionality.

## 🎯 Method Demo: Real vs Generated

<table>
  <tr>
    <th>Real Image</th>
    <th>Generated Image</th>
  </tr>
  <tr>
    <td><img src="assets/yud_example.jpg" width="300"/></td>
    <td><img src="assets/dalle3_example.png" width="300"/></td>
  </tr>
  <tr>
    <th>Real Output (correct Manhattan Frame)</th>
    <th>Generated Output (incorrect Manhattan Frame)</th>
  </tr>
  <tr>
    <td><img src="assets/yud_output.png" width="300"/></td>
    <td><img src="assets/dalle3_output.png" width="300"/></td>
  </tr>
</table>