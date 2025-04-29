import numpy as np
from sklearn.preprocessing import StandardScaler

# Takes cleaned data and finds the min and max of each column's values
# Then applies a scaling factor with Scikit's standard Scaler
# Outputs scaled data to scaled.data

with open('./dataset/cleaned.data', 'r') as input:
    with open('./dataset/scaled.data', 'w') as output:
        fulldata = []
        for line in input:
            line = line.replace('\n', "")
            line = line.split(',')

            fulldata.append(line)
        
        mynparray = np.array(fulldata) # converts all of the dataset into a 2d np array
        scaler = StandardScaler()
        scaled = scaler.fit_transform(mynparray)
        scaled = scaled.tolist() # needs to convert all the numbers back to a normal python list

        # writes to the scaled.data file
        for line in scaled:
            line = list(map(str, line)) # also needs to convert all numbers into strings again
            output.write(','.join(line) + '\n')



                
