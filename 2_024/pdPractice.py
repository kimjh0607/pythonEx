import pandas as pd

#dictionary of data
data = {'name' : ['A','B','C','D'],
        'age'  : [25, 30, 35, 40],
        'gender' : ['F', 'M', 'M', 'F']}

#dataFrame from the dictionary
df = pd.DataFrame(data)

#print the dataFrame
print(df)

#print the mean age of the people in the dataFrame
print('Mean age : ', df['age'].mean())


hw_finished = False
if hw_finished :
        print('Good job!')
else :
        print('Keep going!')