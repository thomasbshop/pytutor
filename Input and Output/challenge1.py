# write a program to append the times table to our jabberwocky poem
# in sample.txt. We want the tables from 2 to 12(similar to the output from loops)
# The first column of numbers should be right justified

with open("/home/thomasj/Desktop/py tutor/py/tutorialdev/Input and Output/sample.txt", 'a') as poem_file:

    for i in range(0, 13):
        for j in range(0, 13):
            print("{0} time {1} is {2}".format(i, j, i*j), end='\n', file=poem_file)
        print('='*15, file=poem_file)

