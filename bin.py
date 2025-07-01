import random as rdm
# code that defines a function that takes in 4 arguments (number of entries in list, bin width, 
# minimum/maximum random number generated) and outputs a dictionary with keys as bin ranges and values 
# as the numbers that show up within the given bin range
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
        bin1 = nummin + (n-1)*binwidth # defining vars bin1 and bin2 because they show up a lot in calcs
        bin2 = nummin + n*binwidth - 1
        if nummin + n * binwidth <= nummax:
            mydict[f"{bin1}-{bin2}"] = []
        else:
            mydict[f"{bin1}-{nummax}"] = []
        for element in mylist:
            if nummin + n * binwidth <= nummax:
                if element >= bin1 and element < nummin + n*binwidth:
                    mydict[f"{bin1}-{bin2}"].append(element)
            else:
                if element >= bin1 and element < nummin + n*binwidth:
                    mydict[f"{bin1}-{nummax}"].append(element)
        n += 1
    return mydict

u = orglist(10, 2, 2, 7)
print(u)