import zlib

s = b'witch which as which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))
print(zlib.crc32(s))  # 3827263511
