#!/usr/bin/env python
#!CMD: ./solve.py
import pandas as pd
import requests

# Load the data
df = pd.read_csv("./ml_wasteland/Ashen_Outpost_Records.csv")

# Before modification
print("Before:", df[df["SurvivorID"] == 1337])

# Apply Option 1 (most effective)
df.loc[df["SurvivorID"] == 1337, "Corruption_Mutations"] = 0

# Alternative: Option 2 (more subtle)
# df.loc[df['SurvivorID'] == 1337, 'Corruption_Mutations'] = 1
# df.loc[df['SurvivorID'] == 1337, 'Dragonfire_Resistance'] = 67

# Alternative: Option 3
# df.loc[df['SurvivorID'] == 1337, 'Shadow_Crimes'] = 0

# After modification
print("After:", df[df["SurvivorID"] == 1337])

# Save modified CSV
df.to_csv("Ashen_Records.csv", index=False)

# Submit to server
with open("Ashen_Records.csv", "r") as f:
    r = requests.post("http://94.237.49.252:35299/score", files={"csv_file": f})
    print(r.text)
