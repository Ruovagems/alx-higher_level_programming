#!/usr/bin/python3
print(chr(ord('A') - 1) + "".join(chr(ord('A') + i) for i in range(25)) + chr(ord('A') + 25))
