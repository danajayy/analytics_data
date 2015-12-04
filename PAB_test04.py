#!/usr/local/isip/tools/common/anaconda/bin/python

# file: !/home/nedc/Documents/Temple_Analytics/PAB_test04.py
#
# revision history: 
#  20151018 (WO): initial version 
#
# In this program, I sort the columns of  PAB_Ticket_Sales.csv into their own lists and sets. 
# Additionally, I count the occurrances of the names of the shows to determine which shows 
# attracted the most ticket orders. 
#------------------------------------------------------------------------------------------------

# Import important modules
#
import sys
import csv 
from collections import Counter 

# Define global TRUE, FALSE, and DEBUG 
#
TRUE = 1
FALSE = 0
DEBUG = FALSE

def main(argv):

    # Open Python_test01.csv to be read as an object with
    # the name 'file'
    #
    file = open('PAB_Ticket_Sales.csv','rb') 
    
    # Establish empty lists for the different catagories in the PAB
    # ticket sales documentation
    #
    perf_no = []
    perf_desc = []
    perf_dt = []
    customer_no = []
    city = []
    state = []
    postal_code = []
    order_no = []
    order_dt = []
    num_seats = []
    paid_flag = []
    mos = []
    mos_desc = []
    price_type = []
    price_type_desc = []
    tot_due_amt = []
    tot_bal_amt = []
    pmt_method_desc = []
    zmap = []
    source_name = []

    # Execute the code in the 'try' statement
    #
    try:

        # Assign reader object for file to be 'reader'
        #
        reader = csv.reader(file)

        # Iterate through the entirety of the PAB ticket sales
        #
        for row in reader:
            
            # Populate lists with input from each row
            #
            perf_no.append(row[0])
            perf_desc.append(row[1])
            perf_dt.append(row[2])
            customer_no.append(row[3])
            city.append(row[4])
            state.append(row[5])
            postal_code.append(row[6])
            order_no.append(row[7])
            order_dt.append(row[8])
            num_seats.append(row[9])
            paid_flag.append(row[10])
            mos.append(row[11])
            mos_desc.append(row[12])
            price_type.append(row[13])
            price_type_desc.append(row[14])
            tot_due_amt.append(row[15])
            tot_bal_amt.append(row[16])
            pmt_method_desc.append(row[17])
            zmap.append(row[18])
            source_name.append(row[19])

        #
        # End for loop

        # Print order cities (city) to check functionality
        #
        if DEBUG:
            print city

        # Hand off performance description list to separate function 
        # to be counted, generating histogram of performace titles
        #
        perf_desc_hist = histogram(perf_desc)
        print perf_desc_hist 

        # Hand off performance date list to separate function to be 
        # counted, generating histogram of performance dates
        #
        perf_dt_hist = histogram(perf_dt)
        print perf_dt_hist

    #
    # End try statement

    # Define clean-up action to close file
    #
    finally:
        file.close()

#
# End of main()

# This function counts the number of occurances in a list
#
def histogram(arg):

    # Establish counter object
    #
    cnt = Counter()

    # For each word in the argument list, increase it's occurance in cnt
    # by one
    #
    for word in arg:
        cnt[word] += 1

    # Return counter object 'cnt' to main
    #
    return cnt 
    
#
# End of histogram()

# begin gracefully, THIS STATEMENT MUST BE LAST.
#
if __name__ == "__main__":
    main(sys.argv[0:])

#
# EOF





