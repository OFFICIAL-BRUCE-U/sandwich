#sandwich will be our method for add string inbetween words in strings.
#loaf will be the original string
#filling will be the string to add inbetween words
def sandwich(bread,filling):
    #crust is a library of bread, split into individual strings a
    crust = bread.split()
    #enumerate iterates through crust, index by index
    for index, value in enumerate(crust):
        #f string adds filling after each string in crust, as enumerate loop iterates through library
        crust[index] = f"{crust[index]} {filling}"
    #lunch rejoins our new string together 0 + filling + 1 + filling + ...
    #we add spaces maunally here
    lunch = ' '.join(crust)
    #final result is printed, filling at start is added manually
    print(filling + " " + lunch)
sandwich("what the deme doing?", "demeStutter")