# Environment Setup Guide (Conda & Jupyter)

This guide documents the isolated environment setup used for the experimental notebooks and scripts in this module. It ensures full reproducibility for evaluation and execution.

---

## Prerequisites

* **Conda:** Miniconda or Anaconda installed.
* **Python Target:** Python `3.11` (recommended for modern LangChain and AI library compatibility).

---

## Quick Setup

### 1. Accept Anaconda Terms of Service (if prompted)
On recent Conda versions, accept the default channel terms if running for the first time:

```bash
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
```

### 2. Create the Conda Environment
Create an isolated environment named `langagent`:

```bash
conda create -n langagent python=3.11 -y
```

### 3. Activate the Environment
```bash
conda activate langagent
```

---

## Dependencies & Jupyter Kernel Integration

To run the notebooks in this directory using the dedicated `langagent` environment:

### 1. Install Project Dependencies & Jupyter Kernel Support
```bash
pip install -r ../requirements.txt
pip install ipykernel jupyter
```

### 2. Register the Kernel with Jupyter
Register `langagent` so it appears in your Jupyter / VS Code / Cursor kernel selector:

```bash
python -m ipykernel install --user --name=langagent --display-name="Python (langagent)"
```

---

## Verification

Verify that the active interpreter matches the environment:

```bash
which python
# Expected output: /home/<user>/miniconda3/envs/langagent/bin/python

python -c "import sys; print(f'Python version: {sys.version}')"
```

---

## Maintenance & Teardown

* **Deactivate environment:**
  ```bash
  conda deactivate
  ```
* **Remove environment (if resetting):**
  ```bash
  conda env remove -n langagent
  ```
* **Remove Jupyter kernel:**
  ```bash
  jupyter kernelspec uninstall langagent -y
  ```
