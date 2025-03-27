#!/usr/bin/env python
#!CMD: ./solve.py

import torch
import builtins

# Store the original exec function
original_exec = builtins.exec

# Replace exec with print
builtins.exec = lambda code, *args, **kwargs: print(f"[EXEC CAPTURED]: {code}")

try:
    # Now when the pickle loads and tries to call exec, it will print the code instead
    model = torch.load("resnet18.pth", weights_only=False, map_location="cpu")
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
finally:
    # Restore the original exec function
    builtins.exec = original_exec
