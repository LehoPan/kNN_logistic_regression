# Takes input data, and removes uneccessary patient ID column and encodes the Benign and Malignant column to 0 and 1 repectively
# Writes new data to cleaned.data, and the B/M column as the labels to labels.data

with open('./dataset/wdbc.data', 'r') as input:
    with open('./dataset/cleaned.data', 'w') as output:
        with open('./dataset/labels.data', 'w') as labeloutput:
            # cut off the labels column into its own file
            labelarr = []

            # cycles through every row of the data
            for line in input:
                line = line.replace('\n', "")
                line = line.split(',')
                line.pop(0) # removes unnecessary ID column

                # one-hot encodes the Malignant and Benign labels to numerical values
                if line[0] == 'M':
                    labelarr.append('1')
                elif line[0] == 'B':
                    labelarr.append('0')

                line.pop(0) # fully removes the labels column
                output.write(','.join(line) + '\n') # writes the cleaned data to cleaned.data
            labeloutput.write(','.join(labelarr)) # writes the labels to labels.data
            