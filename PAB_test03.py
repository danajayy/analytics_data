#!/usr/local/isip/tools/common/anaconda/bin/python

# file: !/home/nedc/Documents/Temple_Analytics/PAB_test03.py
#
# revision history: 
#  20151018 (WO): initial version 
#
# In this program, I sort the columns of  PAB_Ticket_Sales.csv into their own lists and sets
# to be sorted in a future program. This program uses the set to isolate all the misspellings 
# in the data set which I then correct manually. NOPE NOPE NOPE THIS IS DONE
#------------------------------------------------------------------------------------------------

# Import important modules
#
import sys
import csv 

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

        # Convert each list to a set, this isolates copies of words which will indicate misspellings
        #
        perf_no_set = set(perf_no)
        perf_desc_set = set(perf_desc)
        perf_dt_set = set(perf_dt) 
        customer_no_set = set(customer_no)
        city_set = set(city)
        state_set = set(state)
        postal_code_set = set(postal_code)
        order_no_set = set(order_no)
        order_dt_set = set(order_dt)
        num_seats_set = set(num_seats)
        paid_flag_set = set(paid_flag)
        mos_set = set(mos)
        mos_desc_set = set(mos_desc)
        price_type_set = set(price_type)
        price_type_desc_set = set(price_type_desc)
        tot_due_amt_set = set(tot_due_amt)
        tot_bal_amt_set = set(tot_bal_amt)
        pmt_method_desc_set = set(pmt_method_desc)
        zmap_set = set(zmap)
        source_name_set = set(source_name)

        # Print cities set (city_set) to check misspellings
        #
        print city_set
        print len(city_set)

        # Hand off cities list to separate function to be corrected
        #
        correct_cities(city)

    #
    # End try statement

    # Define clean-up action to close file
    #
    finally:
        file.close()

#
# End of main

# This function corrects the misspellings in city names
#
def correct_cities(arg):

    # For a certain word at index value 'i' in a numbered list
    # 'arg'...
    #
    for i,word in enumerate(arg):

        # Replace misspelled word with correct one
        #
        if word == 'Eht':
            arg[i] = 'Egg Harbor Township' 
        if word == 'W Hartford':
            arg[i] = 'West Hartford' 
        if word == 'Haddon Twp':
            arg[i] = 'Haddon Township'
        if word == 'Cinniminson':
            arg[i] = 'Cinnaminson'
        if word == 'bryn mawr':
            arg[i] = 'Bryn Mawr' 
        if word == 'Vilanova':
            arg[i] = 'Villanova' 
        if word == 'Yardley, PA':
            arg[i] = 'Yardley'
        if word == 'Montrose st':
            arg[i] = 'Montrose Street'
        if word == 'Ft Washington':
            arg[i] = 'Fort Washington'
        if word == 'San francisco':
            arg[i] = 'San Francisco'
        if word == 'Philadelphiaphiladelphia':
            arg[i] = 'Philadelphia'
        if word == 'Cinaminson':
            arg[i] = 'Cinnaminson'
        if word == 'Somers point':
            arg[i] = 'Somers Point'
        if word == 'Trescott TWP':
            arg[i] = 'Trescott Township'
        if word == 'Wrigthsville':
            arg[i] = 'Wrightsville'
        if word == 'hatfield':
            arg[i] = 'Hatfield'
        if word == 'Toms river':
            arg[i] = 'Toms River'
        if word == 'Newtown Sq':
            arg[i] = 'Newtown Square'
        if word == 'Phiadelphia':
            arg[i] = 'Philadelphia'
        if word == 'Gwynedd valley':
            arg[i] = 'Gwynedd Valley'
        if word == 'Hosham':
            arg[i] = 'Horsham'
        if word == 'Ft Washington':
            arg[i] = 'Fort Washington'
    
#
# End of correct_cities

# begin gracefully, THIS STATEMENT MUST BE LAST.
#
if __name__ == "__main__":
    main(sys.argv[0:])

#
# EOF





