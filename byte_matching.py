#!PythonProjects/env python
# Davenport University
# Class Info: CISP253-23151 (Winter 2022)
# Author: Alexander Rogers
# Contact: arogers23@email.davenport.edu

# Program name: byte_matching.py
"""
Example of how a Python programs can functions to open a file, locate specified values of data (in this case binary
strings), and return information about the data.
"""

# Import the necessary modules, in this case regular expressions (re), and math.
import re
import math


def match_again():
    """
        match_again function with if/elif/else statements to take user input to either run the match function again
        or exit the program.
            Vars:
                match_again_input: This takes input from the user and asks them to pick either running the program
                again or end the program.
            if/else/elif:
                The statements return the actions of the users input from the match_again_input variable.
    """

    match_again_input = input('''Run byte match again? Y or N''')

    if match_again_input.upper() == 'Y':
        match()
        match_again()
    elif match_again_input.upper() == 'N':
        print('End.')
        exit()
    else:
        match_again()


def match():
    """
        match function performs bit matching, binary output, decimal conversion, and line number output. It is used to
        locate all matching binary values in the Binary.txt, which can be set to any binary values, as long as the
        range of binary values is updated. This also includes matching binary values in different byte positions in a
        line of binary. This module also implements regular expression operations and math operations. The bytepos
        equation occurs before the if statement to aid in differentiating the actual byte position. Therefore additional
        +1 since bytepos would be 0 if not, referring to an incorrect position.
            Vars:
                binfile: The variable which stores the text as a string from binary.txt.
                m_find: This variable is the users input, which is compared against all the values in the text file.
                counter: This variable counts the number of lines in the text file.
                index: This variable checks for the length of each line, and determines when to move on.
                prev: This variable is the length of the index, plus the length of the input of m_find.
                position: This variable is the retrieved input of the user which is read from the text file.
                int_val: This variable is conversion of the binary string into an integer value based on its length.
                bytepos: This variable is the byte position where the user input is in the line of a binary string.
            if/else/elif:
                The statements return the conversions of the binary strings in the text file. This should be testable
                by converting the binary string into an integer by hand or calculator. The value is dependent on the
                length of the input being searched for in the text file as well.
            While:
                While the index is less than the length of the line being read from the text file, and not equal to -1,
                continue counting the to the length of the line.
            Note: Some binary number may have to be expressed with leading zeros.
    """

    # Initialize lines as an empty list.
    lines = []

    # Open the text file desired.
    with open('Binary.txt', 'rt') as binfile:
        for line in binfile:
            lines.append(line.rstrip('\n'))
        m_find = input("Binary number:")

        # Initialize the counter
        counter = 0
        for line in lines:
            index = 0
            prev = 0
            counter += 1

            # __contains__ essentially checks whether a given substring is part of a string or not.
            if line.__contains__(m_find):

                # Length of 7 digit binary value.
                if len(m_find) == 7:
                    int_val = int(line.strip('0')[:7], 2)
                    print("Integer Value:", int_val)

                # Length of 8 digit binary value.
                elif len(m_find) == 8:
                    int_val = int(line.strip('0')[:8], 2)
                    print("Integer Value:", int_val)

                # Length of 9 digit binary value.
                elif len(m_find) == 9:
                    int_val = int(line.strip('0')[:9], 2)
                    print("Integer Value:", int_val)

                # Length of 10 digit binary value.
                elif len(m_find) == 10:
                    int_val = int(line.strip('0')[:10], 2)
                    print("Integer Value:", int_val)

                # Length of 11 digit binary value.
                elif len(m_find) == 11:
                    int_val = int(line.strip('0')[:11], 2)
                    print("Integer Value:", int_val)

                # Length of 12 digit binary value.
                elif len(m_find) == 12:
                    int_val = int(line.strip('0')[:12], 2)
                    print("Integer Value:", int_val)

                # Length of 13 digit binary value.
                elif len(m_find) == 13:
                    int_val = int(line.strip('0')[:13], 2)
                    print("Integer Value:", int_val)

                # Length of 14 digit binary value.
                elif len(m_find) == 14:
                    int_val = int(line.strip('0')[:14], 2)
                    print("Integer Value:", int_val)

                # Length of 15 digit binary value.
                elif len(m_find) == 15:
                    int_val = int(line.strip('0')[:15], 2)
                    print("Integer Value:", int_val)

                # Length of 16 digit binary value.
                elif len(m_find) == 16:
                    int_val = int(line.strip('0')[:16], 2)
                    print("Integer Value:", int_val)

                position = line.find(m_find)
                bytepos = math.ceil(position / 8)

                # Redundancy to ensure that bytepos cannot default to 0 if the value is within a certain range of
                # math.ceiling.
                if bytepos == 0:
                    print(re.findall('........', line))
                    print("Byte Position:", bytepos + 1)
                    print("Binary:", line.strip('0'))
                    print("Line #:", counter, "\n")
                    continue
                else:
                    print(re.findall('........', line))
                    print("Byte Position:", bytepos)
                    print("Binary:", line.strip('0'))
                    print("Line #:", counter, "\n")
                    continue

            while index < len(line):
                index = line.find(m_find, index)
                if index == -1:
                    break
                print(" " * (index - prev), end='')

                prev = index + len(m_find)
                index += len(m_find)


match()
match_again()
