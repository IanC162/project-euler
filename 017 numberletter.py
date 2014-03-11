#Problem: compute the sum of numbers of letters of the integers from 1 to 1000
#Note: "And" is used with British usage

nums = {
    1 : 3,
    2 : 3,
    3 : 5,
    4 : 4,
    5 : 4,
    6 : 3,
    7 : 5,
    8 : 5,
    9 : 4,
    0 : 0
}

tens = {
    1 : 3,
    2 : 6,
    3 : 6,
    4 : 5,
    5 : 5,
    6 : 5,
    7 : 7,
    8 : 6,
    9 : 6,
    0 : 0
}

teens = {  
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8
}

def letters(n):
    if len(str(n)) == 1:
        return nums[n]
    elif len(str(n)) == 2:
        if n >= 20:
            return tens[int(str(n)[0])] + nums[int(str(n)[1])]
        else:
            return teens[n]
    elif len(str(n)) == 3:
        if n % 100 == 0:
            return nums[int(str(n)[0])] + 7
        elif (int(str(n)[1:3]) < 20) and (int(str(n)[1:3]) > 9):
            return nums[int(str(n)[0])] + 10 + teens[int(str(n)[1:3])]
        else:
            return nums[int(str(n)[0])] + 10 + tens[int(str(n)[1])] + nums[int(str(n)[2])]
    else:
        return 11

print sum([letters(n) for n in range(1,1001)])
raw_input()
