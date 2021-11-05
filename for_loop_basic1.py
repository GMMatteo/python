"""
Basic - Print all integers from 0 to 150.
Multiples of Five - Print all the multiples of 5 from 5 to 1,000
Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""

for i in range(151):
    print(i)

for x in range(5,1001,5):
    print(x)

for z in range (1,101,1):
    if z % 5 == 0:
        if z% 10 == 0:
            print ('Coding Dojo')
    else:
        print(z)
    if z % 5 == 0:
        if z % 10 != 0:
            print ('Coding')

maximum = int(500000)
sum = 0
number = 1

while number <= maximum:
    if(number % 2 != 0):
        sum = sum + number
    number = number + 1

print((sum))

for j in range(2018, 0, -4):
    print(j)

lowNum = 1
highNum = 18
mult = 2

for y in range(lowNum, highNum + 1):
    if y % mult == 0:
        print(y)