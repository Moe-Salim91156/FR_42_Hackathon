# %% [code] {"execution":{"iopub.status.busy":"2025-05-17T20:21:44.119474Z","iopub.execute_input":"2025-05-17T20:21:44.119857Z","iopub.status.idle":"2025-05-17T20:21:44.126113Z","shell.execute_reply.started":"2025-05-17T20:21:44.119827Z","shell.execute_reply":"2025-05-17T20:21:44.125103Z"}}
import json
import pandas as pd
from pathlib import Path
from fastai.vision.all import *
from torchvision.models import ResNet50_Weights

# %% [code] {"execution":{"iopub.status.busy":"2025-05-17T20:21:44.127806Z","iopub.execute_input":"2025-05-17T20:21:44.128194Z","iopub.status.idle":"2025-05-17T20:21:44.157914Z","shell.execute_reply.started":"2025-05-17T20:21:44.128132Z","shell.execute_reply":"2025-05-17T20:21:44.156929Z"}}
dataset_root ='./'

with open(dataset_root + 'cleanAmman.json') as f:
    data = json.load(f)

df = pd.DataFrame(data)



# %% [code] {"execution":{"iopub.status.busy":"2025-05-17T20:21:44.159081Z","iopub.execute_input":"2025-05-17T20:21:44.159423Z","iopub.status.idle":"2025-05-17T20:21:46.151287Z","shell.execute_reply.started":"2025-05-17T20:21:44.159391Z","shell.execute_reply":"2025-05-17T20:21:46.150077Z"}}
dblock = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_x=ColReader('image_path'),
    get_y=ColReader('kind'),
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    item_tfms=Resize(128),
    batch_tfms=aug_transforms()
)
dls = dblock.dataloaders(df, bs=32)

# %% [code] {"execution":{"iopub.status.busy":"2025-05-17T20:27:39.949915Z","iopub.execute_input":"2025-05-17T20:27:39.950679Z","iopub.status.idle":"2025-05-17T20:28:12.374406Z","shell.execute_reply.started":"2025-05-17T20:27:39.950644Z","shell.execute_reply":"2025-05-17T20:28:12.373059Z"}}
vision_learner(dls,models.resnet50, pretrained=True, weights='IMAGENET1K_V2')
