#Create a set of all numbers in list. 

#use compare below to look for those numbers and count their instances..

from typing import Counter


def compare(counta): # looking through each list for ascending numbers
    sety = set(counta)
    return sety

toto = []
sety = {}
def totals(counter):
    global toto
    toto.append(counter)
    
def form(listy):
    global sety
    global counter
    counter=[]
    factor = 2
    counta = []
    for number in listy:
        while number !=1:
            if number % factor == 0:
                number = number/factor
                counter.append(factor)
                counta.append(factor)
                factor = 2
            else:
                factor += 1       
        totals(counter)
        sety = compare(counta) 
        counter = []
        

#input Numbers and terminate with #
listy =[]
inp = input('Enter numbers, terminate with #\n>> ')
if inp != '#':
    listy.append(int(inp))
while inp != "#":
    inp = input('Enter numbers, terminate with #\n>> ')
    if inp != '#':
        listy.append(int(inp))

#Send to formula and print
form (listy)

total = 1
for num in sety: #from here fix
    scount = 0 
    for subl in toto:
        s2count = subl.count(num)
        if s2count > scount:
                scount = s2count
    if scount > 0:
        total = total*(num**scount)

print ('The LCM of',listy,'is',total)
