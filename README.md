# CS413 Project: Estimating Manhattan frames to analyze structural inconsistencies

We use vanishing points and camera intrinsics to extract the dominant manhattan frame in an image to test the orthogonality constraints expected from real-world architectures. This method obtained an F1-Score of 0.75 on a mixed real/generated images handmade benchmark. This method showed signs of robustness to resampling, a common weakness of classical learning-based detectors, although more work is needed to explore it.
## 🛠 Installation

```bash
git clone --recurse-submodules git@github.com:Tetchki/cs413-project.git
cd cs413-project
```

1. Create a Python 3.12 virtual environment.

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download DeepLSD model weights:

   ```bash
   python3 download_deeplsd_weights.py
   ```

## 📁 Data

* The `data/` directory contains the datasets used for finetuning and evaluation.
* YOu can download the full data folder from [here](https://drive.google.com/drive/folders/1KE5jK0FZSqztiJwzxzEN0hkqLp3hMu_C?usp=sharing).
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