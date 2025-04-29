# the dataset labels that there is no missing data here, but we will check anyway
# it will scan all the data and return if it is missing any columns in any of the rows
with open('./dataset/wdbc.data', 'r') as input:
    i = 0 # for keeping track of which row we are on
    for line in input:
        line = line.split(',')
        i += 1
        if len(line) != 32:
            print(f"WARNING: Row {i} is missing or has additional columns!")
            i = None
            break
    if i != None:
        print("Data is full and no missing or extra columns!")