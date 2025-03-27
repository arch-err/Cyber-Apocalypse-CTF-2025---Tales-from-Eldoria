#!/usr/bin/env python
#!CMD: ./solve.py
import torch
import torch.nn as nn
import torchvision.models as models

# Create a ResNet18 model with the same structure
resnet = models.resnet18(pretrained=False)

# Load the state dict
resnet.load_state_dict(model)
resnet.eval()

# Try specific inputs that might trigger the flag
# In CTF challenges, sometimes all-zero, all-one, or specific test images work
zero_input = torch.zeros(1, 3, 224, 224)
output = resnet(zero_input)

# Check output for unusual patterns
print(output)
