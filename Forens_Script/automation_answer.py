from pwn import *
import struct

p = remote('ip', port)
p.recv()

ans = [
    'example1',
    'example2',
]

for i in ans:
    p.sendline(i.encode())
    print(i)
    print(p.recv())