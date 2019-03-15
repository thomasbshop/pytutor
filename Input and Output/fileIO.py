# reading text files
jabber = open("/home/thomasj/Desktop/py tutor/py/tutorialdev/Input and Output/sample.txt", "r")
# for line in jabber:
#     print(line)

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end=' ')

# jabber.close()

with open("/home/thomasj/Desktop/py tutor/py/tutorialdev/Input and Output/sample.txt") as jabber1:
    for line in jabber1:
        if "JAB" in line.upper():
            print(line, end=' ')

# no need to close the file here because the 'with' has already taken care of it
print('-' * 40)
with open("/home/thomasj/Desktop/py tutor/py/tutorialdev/Input and Output/sample.txt") as jabber2:
    line = jabber2.readline()
    while line:
        print(line, end='')
        line = jabber2.readline()

print('-' * 40)

# inefficient for large files
with open("/home/thomasj/Desktop/py tutor/py/tutorialdev/Input and Output/sample.txt") as jabber3:
    lines = jabber3.readlines()
print(lines)

for line in lines:
    print(line, end='')

with open("/home/thomasj/Desktop/py tutor/py/tutorialdev/Input and Output/sample.txt") as jabber4:
    lines = jabber4.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')

# reverse using .read()
with open("/home/thomasj/Desktop/py tutor/py/tutorialdev/Input and Output/sample.txt") as jabber5:
    lines = jabber5.read()

for line in lines[::-1]:
    print(line, end='')
