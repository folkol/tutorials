import struct
import sys

print(sys.byteorder)  # little

with open('test.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):  # Show the first 3 file headers
    start += 14
    """
        H: 2 byte unsigned
        I: 4 byte unsigned
        <: little-endian and 'standard size'
    """
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filename_size, extra_size = fields

    start += 16
    filename = data[start:start+filename_size]
    start += filename_size
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size
