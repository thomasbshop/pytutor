# when writing code break the problem into small manageable tasks


def python_food():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


python_food()


def center_text(*args, sep=' ', end='\n', file=None, flush=False):  # the asteric indicates take many arguments
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, sep=sep, end=end, file=file, flush=flush)


with open("centered", mode='w') as centered_file:  # send the output to a file

    center_text(1, 2, 3, 4, 5, 6, sep=':', file=centered_file)
    center_text("spam and eggs", file=centered_file)
    center_text("spam, spam and eggs", file=centered_file)
    center_text(23, file=centered_file)
    center_text("spam, spam, spam, and spam", file=centered_file)


def solution1(N):
    # write your code in Python 3.6
    # pass
    # groups = []

    this_list = [N[a+1:] for a in range(len(N)) if (int(N[a]) == 1 and int(N[a+1]) == 0)]

    return this_list


def solution(N):
    # write your code in Python 2.7

    binary_string = str(bin(N)).strip("0b")

    string_length = len(binary_string)
    bin_gap = 0
    temp=0
    for i in range(string_length):

        if binary_string[i] == "0":
            bin_gap += 1
        if binary_string[i] == "1":
            if temp < bin_gap:
                temp = bin_gap
            bin_gap = 0
    return temp


solution(1042)



u = ["B", "D", "A", "E", "C"]


def func(u):
    y=[]
    count=65
    while len(y)<len(u):
        for i in u:
            if ord(i)==count:
                y.append(i)
                count+=1
    print(y)

