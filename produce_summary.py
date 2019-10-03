def print_delivery_report(day, daily_file):
    """ Prints delivery report 
    """
    print("Day", day)
    the_file = open(daily_file) # open daily text data file to use in python
    for line in the_file: # iterate each line in 5/19 file
        line = line.rstrip() # strips right whitespaces
        words = line.split('|') # turn string into list at every '|'

        melon = words[0] 
        count = words[1] # changed 0 index to 1
        amount = words[2] # changed 0 index to 2

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount)) # print report
    the_file.close() # close each file

# call functions for each day
print_delivery_report(1, "um-deliveries-20140519.txt")
print_delivery_report(2, "um-deliveries-20140520.txt")
print_delivery_report(3, "um-deliveries-20140521.txt")