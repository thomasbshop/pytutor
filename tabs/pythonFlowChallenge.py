"""
create a program that takes an ip address entered at the keyboard and prints out the number of segments it contains, and
the length of each segment.
An IP address consists of 4 numbers, separated from each other with a full stop. But your program should just count
however many are entered
Examples of input you may get are:
127.0.0.1
192.168 0.1
10.0.12345.255
172.18
255

So your program should work even with invalid Ip addresses. We are just interested with the number of segments and how
 long each one is.
Once you have a working program here are some of the suggestions for invalid input to test:
.123.45.678.92
123.4567.8.9
123.156.289.123242143
10.10t.10.10
12.9.34.6.12.90
'' - i.e. press enter without typing anything

This challenge is intended to practice for loops and if/else statements, so although you could use another technique
(such as splitting and string up), thats not the uproach we are looking for here.
"""
input_prompt = ("An IP address consists of 4 numbers, separated from each other with a full stop."
                "please enter your your IP address: ")
ip_address = input(input_prompt)
segment = 1
segment_length = 0
# initialise character
character = ""

for character in ip_address:
    if character == ".":
        print("segment {0} contains {1} characters ".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

# unless the final character in the string was a . then we haven't printed the last segment
if character != ".":
    print("segment {0} contains {1} characters ".format(segment, segment_length))


# another way to do it
ip_address2 = input("please enter another IP address: ")
if ip_address2[-1] != ".":
    ip_address2 += "."

segment2 = 1
segment_length2 = 0


for character in ip_address2:
    if character == ".":
        print("segment {0} contains {1} characters ".format(segment2, segment_length2))
        segment2 += 1
        segment_length2 = 0
    else:
        segment_length2 += 1

