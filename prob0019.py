# project euler, problem 19

DOWS = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
MONTH_LEN = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP_MONTH_LEN = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_month_days(year, start_day):
        dow = []
        sum = start_day

        if (year % 100 != 0) and (year % 4 == 0):
                lengths = LEAP_MONTH_LEN
                leap = True
        elif year % 400 == 0:
                lengths = LEAP_MONTH_LEN
                leap = True
        else:
                lengths = MONTH_LEN
                leap = False

        dow.append(start_day)
        for i in range(0, len(lengths)-1):
                month_len = lengths[i]
                sum = sum + month_len
                dow.append(sum % 7)

        return (dow, (sum + lengths[len(lengths)-1]) % 7, leap)

def main():
        start_day = 1
        sundays = 0
        leap = False
        for i in range(1901, 2001):
                (dow, next_start_day, leap) = get_month_days(i, start_day)
                print("year: %d, starting day of weak: %s, leap: %s" % (i, DOWS[start_day], str(leap)))

                for j in dow:
                        print("\t%d" % j)
                        if j == 6:
                                sundays = sundays + 1

                start_day = next_start_day

        print("number of sundays: %d" % sundays)

main()
