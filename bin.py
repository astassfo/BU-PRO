import random as rdm
# code that defines a function that takes in 4 arguments (number of entries in list, bin width, 
# minimum/maximum random number generated) and outputs a dictionary with keys as bin ranges and values 
# as counts of numbers generated within its keys bin range.
# NOTE: I am aware that the code is incredibly inefficient.
def orglist(numentries, binwidth, nummin, nummax):
    mylist = [] # initialize unorganized list
    for i in range(numentries):
        mylist.append(rdm.randint(nummin, nummax)) # filling list with random numbers (0-100)
    print("unorganized list:", mylist) # print initial unorganized list
    mydict = {}
    numkeys = int((nummax-nummin) // binwidth + 1) # for correct range of for loop
    n = 1
    for x in range(numkeys):
        count = 0
        u = nummin + (n-1)*binwidth # defining vars bin1 and bin2 because they show up a lot in calcs
        v = nummin + n*binwidth
        # initializing each bin with a count of zero; if-else statement if bin width does not fit evenly 
        # within minimum/maximum number range
        if v <= nummax:
            mydict[f"{u}-{v - 1}"] = count
        else:
            mydict[f"{u}-{nummax}"] = count
        # iterating through every element and placing in correct bin
        for element in mylist:
            if v <= nummax:
                if element >= u and element < v:
                    count += 1
                    mydict[f"{u}-{v - 1}"] = count
            else:
                if element >= u and element < v:
                    count += 1
                    mydict[f"{u}-{nummax}"] = count
        n += 1
    return mydict
# print organized dictionary
example = orglist(5, 3, 1, 10)
print("organized dictionary:", example)