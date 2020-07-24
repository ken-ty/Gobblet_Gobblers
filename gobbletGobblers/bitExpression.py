# coding=utf-8
import numpy as np

MSB = np.uint32(0x04000000)  # Most Significant Bit、最上位ビット
BB_MASK = np.uint32(0xFFFFFFFF)

# ーＡＢＣ
# １・・・
# ２・・・
# ３・・・

A1L = np.uint32(0x04000000)
A1M = np.uint32(0x02000000)
A1S = np.uint32(0x01000000)
B1L = np.uint32(0x00800000)
B1M = np.uint32(0x00400000)
B1S = np.uint32(0x00200000)
C1L = np.uint32(0x00100000)
C1M = np.uint32(0x00080000)
C1S = np.uint32(0x00040000)

A2L = np.uint32(0x00020000)
A2M = np.uint32(0x00010000)
A2S = np.uint32(0x00008000)
B2L = np.uint32(0x00004000)
B2M = np.uint32(0x00002000)
B2S = np.uint32(0x00001000)
C2L = np.uint32(0x00000800)
C2M = np.uint32(0x00000400)
C2S = np.uint32(0x00000200)

A3L = np.uint32(0x00000100)
A3M = np.uint32(0x00000080)
A3S = np.uint32(0x00000040)
B3L = np.uint32(0x00000020)
B3M = np.uint32(0x00000010)
B3S = np.uint32(0x00000008)
C3L = np.uint32(0x00000004)
C3M = np.uint32(0x00000002)
C3S = np.uint32(0x00000001)

EMPTY = np.uint32(0x00000000)

