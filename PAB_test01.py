#!/usr/local/isip/tools/common/anaconda/bin/python

# file: !/home/nedc/Documents/Temple_Analytics/PAB_test01.py
#
# revision history: 
#  20151017 (WO): initial version 
#
# In this program, I print the first 5 (five) rows from the file PAB_Ticket_Sales.csv 
#------------------------------------------------------------------------------------------------

# Import important modules
#
import sys
import csv 

def main(argv):

    # Open Python_test01.csv to be read as an object with
    # the name 'file'
    #
    file = open('PAB_Ticket_Sales.csv','rb') 

    # Attempt to execute the code in the 'try' statement
    #
    try:

        # Assign reader object for file to be 'reader'
        #
        reader = csv.reader(file)

        # print first 5 (five) rows in 'reader'
        #
        for row in range(5):
            print reader.next()

    # Define clean-up action to close file
    #
    finally:

        file.close()

#
# end of main

# begin gracefully, THIS STATEMENT MUST BE LAST.
#
if __name__ == "__main__":
    main(sys.argv[0:])

#
# EOF





