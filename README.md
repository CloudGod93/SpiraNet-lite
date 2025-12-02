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

- Supports Python **3.10** only

- Bundles verified dependency stack:

  - TensorFlow **2.13**
  - OpenCV (headless, fixed version)
  - Pillow
  - pyAesCrypt

- Fully packaged + reproducible wheel builds through `pyproject.toml`

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

Interface matches the original vendor library.
Your existing code basically doesn’t notice the change.

---

## **Environment Requirements**

- Python **3.10**
- TensorFlow **2.13**
- NumPy **1.24.x**
- OpenCV-Python-Headless **4.8.1.78**
- Pillow ≥ 10
- pyAesCrypt

These are auto-installed when installing the wheel.

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

## **GitHub Actions CI**

The repository includes an optional CI workflow that automatically:

- builds the wheel
- installs it just like a real project would
- performs a smoke test import to confirm the binary and Python modules load cleanly

This prevents “it works on my machine” failures when publishing new versions or tags.

### **Workflow Location**

```
.github/workflows/ci.yml
```

### **Workflow Logic**

```yaml
name: SpiraNet-lite CI

on:
  push:
    branches: ["main"]
    tags: ["v*"]
  pull_request:
    branches: ["main"]

jobs:
  build-and-smoke-test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install build tooling
        run: |
          pip install --upgrade pip
          pip install build

      - name: Build wheel + sdist
        run: python -m build

      - name: Install from dist
        run: pip install dist/*.whl

      - name: Smoke test import
        run: python -c "from spiranet_lite import SpiraNetLite; print(SpiraNetLite)"
```

### **Triggering CI**

CI runs on:

- pushes to `main`
- PRs targeting `main`
- tags starting with `v` (e.g., `v0.1.1`)

Tagging a release:

```bash
git tag v0.1.1
git push origin v0.1.1
```

---

## **Why This Exists**

Before this package, every MidWest repo kept its own stray copy of the SpiraLibs binary like a rabid alley cat.
It was chaos.

Now:

- one source of truth
- reproducible installs
- dependency consistency
- safe upgrades
- CI catching breakage before deployment

Everyone sleeps better.

---

## **License**

Proprietary — internal MidWest Machine use only.

---
