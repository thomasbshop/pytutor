powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)

print(powers)

x = int(input("please input an integer: "))
printing = False

for power in powers:
    bit = x // power
    # remove leading zeros
    # remember to run boundary values in tests
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
    x %= power
