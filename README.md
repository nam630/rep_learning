# Universal representation learning for faster RL
## Alex Nam and Alex Loia (CS 230 Fall 2021 Project)

### Info
The `default_curl_v3.ipynb` notebook includes our current implementation of the [CURL](https://github.com/MishaLaskin/curl) architecture (namely, the image encoder) along with our own data augmentations.

The `resnet_pretrained.ipynb` uses the same RL architecture as above but uses a pretrained ImageNet ResNet model as the image encoder, which is used to contrast against the CURL encoder.

The `curl+some_state-cartpole.ipnyb` is similar to the default CURL implementation except some velocity state is added to the image encodings to experiment with whether that is functionally equivalent to frame stacking.

### Setup
Run `conda env create -f environment.yml` and `conda activate cs230proj`. Then, run `jupyter notebook` to open the Jupyter Notebook webpage. Open the different notebooks and enjoy!

Runs on Linux only. May require `xvfb` package on headless systems.
