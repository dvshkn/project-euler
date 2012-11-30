# project euler, problem 17

import sys

ONES = ['one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen',
        'twenty']

TENS = ['ten',
        'twenty',
        'thirty',
        'forty',
        'fifty',
        'sixty',
        'seventy',
        'eighty',
        'ninety']

def englishLen(num):
        one = num % 10
        ten = (num % 100) / 10
        hundo = (num % 1000) / 100
        g = num / 1000
        length = 0

        #print("one: %d, ten: %d, hundo: %d" % (one, ten, hundo))

        if g > 0:
                length = length + len(ONES[g-1])
                length = length + len("thousand")
                sys.stdout.write("%s %s " % (ONES[g-1], "thousand"))

        if hundo > 0:
                length = length + len(ONES[hundo-1])
                length = length + len("hundred")
                sys.stdout.write("%s %s " % (ONES[hundo-1], "hundred"))
                if ten > 0 or one > 0:
                        length = length + len("and")
                        sys.stdout.write("and ")

        if ten >= 2:
                length = length + len(TENS[ten-1])
                sys.stdout.write("%s " % TENS[ten-1])
        else:
                one = one + ten*10

        if one > 0:
                length = length + len(ONES[one-1])
                sys.stdout.write("%s" % ONES[one-1])

        sys.stdout.write(" (%d)\n" % length)
        return length

def main():
        sum = 0
        for i in range(1,1001):
                sum = sum + englishLen(i)

        print(">> sum: %d" % sum)

main()
