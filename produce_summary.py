print("Day 1")
the_file = open("um-deliveries-20140519.txt") # open 5/19 daily text data file to use in python
for line in the_file: # iterate each line in 5/19 file
    line = line.rstrip() # strips right whitespaces
    words = line.split('|') # turn string into list at every '|'

    melon = words[0] 
    count = words[1] # changed 0 index to 1
    amount = words[2] # changed 0 index to 2

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()


print("Day 2")
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()


print("Day 3")
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()
