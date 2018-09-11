import webbrowser

# webbrowser.open("https://www.python.org", new=1)

chrome = webbrowser.get(using='google-chrome')
chrome.open_new("https://www.python.org")
#
# help(webbrowser)

# when the term high-level interface is used , they maen that you don't need to understand some protocols such as
# networking, or transport protocols

# it is possible to create our .py file and import it as script in other document

for i in range(10):
    print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep=";", end=" end \n")  # you can provide several objects and/or parameters
                                                              # separated by commas
    # print(range(5::-1))

# the .register() function can be used to make known browsers that are absent in the library available
