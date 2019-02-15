from timeit import default_timer


# ===========================================================
# FUNCTION: under_thousand_to_string
# ===========================================================
#
#  Input:   integer n to be converted to the British-English
#           standard in text from
#
#  Output:  string conversion of the input n in British-
#           English standard in text form
#               eg. 145 = "One-Hundred and forty five"
#
#  Task:    work on the digits from thousands->hudreds->tens
#           ->ones. and add the converted string to the
#           result string, and inserting the "hundred",
#           and "and" appropriately.
#
# ===========================================================
def under_thousand_to_string( n ):
    digits_as_strings =  {
                            0: '',
                            1: 'one',
                            2: 'two',
                            3: 'three',
                            4: 'four',
                            5: 'five',
                            6: 'six',
                            7: 'seven',
                            8: 'eight',
                            9: 'nine',
                            10: 'ten',
                            11: 'eleven',
                            12: 'twelve',
                            13: 'thirteen',
                            14: 'fourteen',
                            15: 'fifteen',
                            16: 'sixteen',
                            17: 'seventeen',
                            18: 'eighteen',
                            19: 'nineteen',
                            20: 'twenty',
                            30: 'thirty',
                            40: 'forty',
                            50: 'fifty',
                            60: 'sixty',
                            70: 'seventy',
                            80: 'eighty',
                            90: 'ninety'
                         }
    as_string         =  ''

    # "one thousand" should be the only n>=1000, so we only consider that
    if n >= 1000:
        as_string  +=  digits_as_strings[ n // 1000 ]
        as_string  +=  " thousand "
        return as_string

    # [Number] hundred (and) ___ ** only consider "and" if not a multiple of 100
    # hundreds digit = (n//10)%10)*10
    if n >= 100:
        as_string  +=  digits_as_strings[ n // 100 ]
        as_string  +=  " hundred "
        n %= 100
        if n is not 0:
            as_string  +=  'and '

    # [Number] hundred and ___ty ___
    if n > 20:
        as_string  +=  digits_as_strings[ n -  n%10 ]
        as_string  +=  ' '
        as_string  +=  digits_as_strings[ n % 10 ]

    # [Number] hundred and [<20, one,two,...,nineteen]
    elif ( n % 100 ) <= 20:
        as_string  +=  digits_as_strings[ n ]

    # Return the number as string
    return as_string


# ===========================================================
# PROBLEM 17 -- Number Letter Counts
# ===========================================================
#
#  If the numbers 1 to 5 are written out in words: one, two,
#  three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
#  letters used total.
#
#  If all numbers from one to 1000 (one thousand) inclusive
#  were written out, how many letters would be used?
#
#  NOTE: Do not count spaces or hyphens. For example, 342
#  (three hundred and forty-two) contains 23 letters and
#  115 (one hundred and fifteen) contains 20 letters. The use
#  of "and" when writing out numbers is in compliance with the
#  British usage
#
# ===========================================================
def problem_17( ):
    # Print Problem Context
    print( "Project Euler Problem 17 -- Number Letter Counts" )

    # Set Up Variables
    start_time   =  default_timer( )
    totalString  =  ''

    # Computation Loop -- Retrieve all Numbers as Strings
    for x in range( 1000 + 1 ):
        totalString  +=  under_thousand_to_string( x )

    # Calculate Results (remove spaces and determine length of total string
    totalString  =  totalString.replace( ' ' , '' )
    result       = len( totalString )

    # Compute Execution Time
    end_time        =  default_timer( )
    execution_time  =  ( end_time - start_time ) * 1000

    # Display Results
    print( "   Total Characters Used:   %d"      %  result )
    print( "   Computation Time:        %.3fms"  %  execution_time )
    return



if __name__ == '__main__':
    problem_17( )