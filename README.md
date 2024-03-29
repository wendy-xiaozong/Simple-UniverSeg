# Simple-UniverSeg
Course Project For ENG EC 500 - Biomedical Images for AI

# Task
To train a simpler variant of UniverSeg, which trains on several labels of 24 seg-protocol of 2D brain MRI and generalize to holdout labels.
![Few Shot Segmentation Task on a Query Image using a Support Set](result/task.jpg)


# Pre-trained UniverSeg Model
The pre-trained UniverSeg model is described at project/models/original_universeg/model.py

# Evaluation Script (project/main.py)
This script evaluates the pre-trained UniverSeg model on [Neurite OASIS Sample Data](https://github.com/adalca/medical-datasets/blob/master/neurite-oasis.md) with 24 seg protocol.

# Utilities scripts (project/utils folder)
- dataset.py: Loads the Neurite OASIS data.
- visualization.py: For visualizing the Original Image, Ground truths, Soft Predictions and Predictions

# path:
```sh
qrsh -P ec500kb -l h_rt=03:00:00 -l mem_per_core=3G -l gpus=1 -l gpu_c=7

module load python3/3.10.12
source /projectnb/ec500kb/projects/UniverSeg/code/project/HWenv/bin/activate
pip install torch torchvision torchaudio

# To run the code
python /projectnb/ec500kb/projects/UniverSeg/code/project/main.py
```
# Plots for visualization (project/Plots)
- choose_labels.ipynb
- plot_selected_labels.ipynb

# Licenses
Code is released under the [Apache 2.0 license](LICENSE).


# Code Details
Adapted Code:
- dataset.py and visualization.py: This code has been modified from the following sources: https://github.com/JJGO/UniverSeg/blob/main/example_data/oasis.py for processing the OASIS dataset.
- OASIS dataset processing details are available at https://github.com/adalca/medical-datasets/blob/master/neurite-oasis.md.
- main.py: The inference pipeline has been adapted from https://colab.research.google.com/drive/1TiNAgCehFdyHMJsS90V9ygUw0rLXdW0r?usp=sharing.

Additional Code:
- main.py: Included Dice Score and HD95 evaluation metrics.
- choose_labels.ipynb: Provides a comparison of the sizes of different Regions of Interest (ROIs) in Brain MRI images.
- plot_selected_labels.ipynb: Highlights labels to provide an overview of the various categories of labelled data.
