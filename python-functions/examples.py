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