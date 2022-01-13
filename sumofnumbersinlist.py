# takes a number and a list and returns the numbers in the list that their sum equals the number passed
def numbers(number, l1):
    xindex = 0
    for x in l1:
        zindex = 0
        for z in l1:
            if xindex == zindex:
                continue
            if x + z == number:
                print(f'{x}+{z}={number}')
            zindex += 1
        xindex += 1


print(numbers(8,[1,2,3,4,5,6,7,10]))
