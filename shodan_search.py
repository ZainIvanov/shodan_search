# To be compatible with Linux and other distros

# !/usr/bin/env python

# Import the shodan library
# and import the sys library

import shodan
import sys


def usage():
    print("[!]Usage: ", sys.argv[0] + " <file_name> <shodan_api_key> <parameters> <number of pages> \n")
    sys.exit()


# Now start the crutial part of the program...
# The code to search using Shodan API

def shodan_search():

    # The first line of code in this function
    # takes the user input (command line arg)
    # and launches off with their api key. lol.

    api = shodan.Shodan(sys.argv[2])

    try:

        # Try to open the file specified in the argv[1]

        result_file = open(sys.argv[1], "w")

        if (result_file == 0):
            print("[!]Cannot open file")
            sys.exit()

        # Else continue on your merry way. :)

        # Basically the next few lines are set of for loops.
        # The first one takes into account the number of pages that is given in argv[4]
        # Than number_of_pages is set to the number of pages.
        # This should work if you have enough credits.
        # If there's not that many pages, it'll throw a error

        for number_of_pages in range(1, int(sys.argv[4])):

            results = api.search(sys.argv[3], page=number_of_pages, limit=None)

            for result in results['matches']:

                result_file.write(result['ip_str'])
                result_file.write("\n")  # Add a newline so that way the IPs show up line by line

    # Or throw an error
    # Usually is caused by non members (didn't pay the one time fee)

    except shodan.APIError as error:  # If a error is thrown, print the error and exit the script

        print("[!]Error: ", error)
        sys.exit()  # Just in case that this program doesn't exit properly


# now the main() function

def main():

    # If no arguments are supplied...
    # Throw a error and exit

    # Also, len is used so that way I can compare the args to usage...
    # If it's less than 2, throw the error

    if (len(sys.argv) < 4):
        usage()

    # Else run through shodan_search()
    shodan_search()


main()