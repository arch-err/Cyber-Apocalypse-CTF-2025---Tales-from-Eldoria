#!/usr/bin/env python
#!CMD: ./solve.py
import torch

# Load the model structure (you might need to define the model architecture first)
model = torch.load("./eldorian_artifact.pth", map_location=torch.device('cpu'))
# Extract the hidden weights
hidden_weights = model['hidden.weight']

# Convert the diagonal values to ASCII characters
message = ""
for row in hidden_weights:
    # Find the non-zero value in each row
    for value in row:
        if value != 0:
            message += chr(int(value))
            break

print(message)

# Print model structure
# print(model)
