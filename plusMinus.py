#Code 1

def plusMinus(arr):
    # Write your code here
    positive = negative = zero = 0
    for x in arr:
        if x>0:
            positive+=1
        elif x<0:
            negative+=1
        else:
            zero+=1
    print(round(positive/n,6))
    print(round(negative/n,6))
    print(round(zero/n,6))
    
    
#Code 2

def plusMinus(arr):
    items = len(arr)
    p = "{0:.6f}".format(len([x for x in arr if x > 0]) / items)
    n = "{0:.6f}".format(len([x for x in arr if x < 0]) / items)
    z = "{0:.6f}".format(len([x for x in arr if x == 0]) / items)

    print("\n".join([p, n, z]))
#this leads to increase in time complexity
    
    
#Code 3

def plusMinus(arr):
    pos = zero = neg = 0
    for value in arr:
        pos += value > 0
        zero += value == 0
        neg += value < 0
        length = len(arr)
    print(round(pos/length, 6))
    print(round(neg/length, 6))
    print(round(zero/length, 6))
    
