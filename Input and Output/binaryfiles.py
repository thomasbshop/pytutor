# processing binary data e.g. image files
# to edit a binary file, specify the mode "b" to indicate binary data
# bytes() built in function converts strings and integers to bytes

with open("binary", 'bw') as bin_file:
    bin_file.write(bytes(range(17)))

with open("binary", 'br') as binFile:
    for b in binFile:
        print(b)

a = 65535  # FF FF
b = 65534  # FF FE
c = 65536  # 00 01 00 00
x = 2998302  # 02 2D C0 1E
# the 2_bytes method converts thee integer to bytes
# the largest number that we can store in two bytes or 16 bits is 65536
with open("binary2", 'bw') as binFile1:
    binFile1.write(a.to_bytes(2, 'big'))
    print(a)
    binFile1.write(b.to_bytes(2, 'big'))
    print(b)
    binFile1.write(c.to_bytes(4, 'big'))
    print(c)
    binFile1.write(x.to_bytes(4, 'big'))
    print(x)
    binFile1.write(x.to_bytes(4, 'little'))
    print(x)

with open("binary2", 'br') as binFile1:
    e = int.from_bytes(binFile1.read(2), 'big')
    print(e)
    f = int.from_bytes(binFile1.read(2), 'big')
    print(f)
    g = int.from_bytes(binFile1.read(4), 'big')
    print(g)
    h = int.from_bytes(binFile1.read(4), 'big')
    print(h)
    i = int.from_bytes(binFile1.read(4), 'big')
    print(i)
