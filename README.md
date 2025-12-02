# **SpiraNet-lite**

`SpiraNet-lite` is a thin Python wrapper around the proprietary **SpiraNetLite** binary used inside MidWest Machine’s production systems (RibbingApp, SteakVision, future CV apps, etc.).
It packages the vendor `.so` and its companion modules into a proper, versioned Python distribution so you can install it cleanly with:

```bash
pip install "git+https://github.com/MidWest-Machine/SpiraNet-lite.git@v0.1.0#egg=spiranet-lite"
```

No more dragging mysterious binaries between repos. No more `sys.path` hacks. No more “where the hell is SpiraLibs today?”

---

## **Features**

- Ships the `SpiraLibs.cpython-310-x86_64-linux-gnu.so` extension

- Includes `SpiraLibsPars.py`, required by the vendor binary

- Exposes a single import:

  ```python
  from spiranet_lite import SpiraNetLite
  ```

- Supports Python **3.10** only (because that’s what the vendor built the binary for)

- Bundles the dependency stack known to work with the binary, including:

  - TensorFlow **2.13**
  - OpenCV (headless)
  - Pillow
  - pyAesCrypt

- Clean wheel builds via `pyproject.toml` + `setuptools`

---

## **Installation**

### **Install directly from GitHub**

```bash
pip install "git+https://github.com/MidWest-Machine/SpiraNet-lite.git@v0.1.0#egg=spiranet-lite"
```

### **Or build locally**

```bash
python -m build
pip install dist/spiranet_lite-0.1.0-*.whl
```

---

## **Usage**

```python
from spiranet_lite import SpiraNetLite

model = SpiraNetLite(weights_folder="/path/to/weights")
result = model.FindFeatures(image)
```

The interface matches the original vendor library, so existing code typically requires no changes beyond replacing the import.

---

## **Environment Requirements**

The packaged binary relies on:

- **Python 3.10**
- **TensorFlow 2.13.x**
- **NumPy 1.24.x**
- **OpenCV-Python-Headless 4.8.x**
- **Pillow**
- **pyAesCrypt**

These are installed automatically when installing the wheel.

If you’re using GPU-enabled TensorFlow, ensure your environment matches your deployment (CUDA/cuDNN versions, drivers, etc.).

---

## **Project Structure**

```
spiranet-lite/
├── spiranet_lite/
│   ├── __init__.py
│   ├── SpiraLibs.cpython-310-x86_64-linux-gnu.so
│   └── SpiraLibsPars.py
├── pyproject.toml
├── MANIFEST.in
└── README.md
```

---

## **Why this exists**

Originally, every MidWest project had its own copy of the vendor binary shoved into a random folder and imported with:

```python
sys.path.append("whatever")
from SpiraLibs import SpiraNetLite
```

That was… bad.

This package:

- centralizes the binary
- cleans up your imports
- ensures deterministic dependency versions
- allows reproducible builds for plant VMs
- avoids “wait which repo has the good SpiraLibs?” chaos

The world becomes slightly more civilized.

---

## **License**

Proprietary — internal MidWest Machine use only.
Redistribution outside the company is not permitted.

---
