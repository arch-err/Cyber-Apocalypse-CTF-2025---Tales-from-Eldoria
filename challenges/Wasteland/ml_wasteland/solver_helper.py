import requests

with open(f"Ashen_Outpost_Records.csv", "r") as f:
	r = requests.post("http://94.237.49.252:35299/score", files={"csv_file": f})
	print(r.text)
