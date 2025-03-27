#!/usr/bin/env python
import torch
import numpy as np
import struct
from torch.serialization import safe_globals

def stego_decode(tensor, n=3):
    bits = np.unpackbits(tensor.view(dtype=np.uint8))
    payload = np.packbits(np.concatenate([np.vstack(tuple([bits[i::tensor.dtype.itemsize * 8] for i in range(8-n, 8)])).ravel("F")])).tobytes()
    (size, checksum) = struct.unpack("i 64s", payload[:68])
    message = payload[68:68+size]
    return message

# First, load the model correctly
with safe_globals(['exec']):
    # We need to load with weights_only=False, but we'll replace exec with a harmless function
    import builtins
    original_exec = builtins.exec

    # This function just returns without doing anything
    builtins.exec = lambda code, *args, **kwargs: None

    try:
        model = torch.load("resnet18.pth", weights_only=False)
        print("Model loaded successfully")
    finally:
        # Restore original exec
        builtins.exec = original_exec

# The model is already a state_dict (OrderedDict), iterate directly
for name, param in model.items():
    try:
        payload = stego_decode(param.data.numpy(), n=3)
        if payload and len(payload) > 10:  # Filter out noise
            print(f"Found payload in tensor: {name}")
            print(f"Decoded payload:\n{payload.decode('utf-8', errors='ignore')}")

            # Write payload to file for inspection
            with open("decoded_payload.txt", "wb") as f:
                f.write(payload)

            # Look for the HTB{} flag format
            decoded_str = payload.decode('utf-8', errors='ignore')
            if 'HTB{' in decoded_str:
                print("FLAG FOUND!")
                # Extract the flag using a simple pattern match
                import re
                flags = re.findall(r'HTB{[^}]*}', decoded_str)
                for flag in flags:
                    print(f"Flag: {flag}")

            break
    except Exception as e:
        print(f"Error processing {name}: {e}")
        continue
