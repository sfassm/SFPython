# SF: First little Python script, based on the information 
# given in this tutorial: http://www.vogella.com/tutorials/Python/article.html
'''
Created on 26 Jul 2017

@author: d069454
'''

# SF: first declare your functions
def add(a,b):
    return a+b

def addFixedValue(a):
    y = 5
    return y +a

# SF: Execute your functions with input values
print add(1,2)
print addFixedValue(1)

# SF: loop
i = 1
for i in range(1, 10):
    if i <= 5 :
        print 'Smaller or equal than 5.\n',
    else:
        print 'Larger than 5.\n',
        
# Concatenate strings:
        
# Using files and comparing strings:
# Reading two files and comparing the comma-separated strings within the string
f1 = open('../samples/pythonstring1.txt', 'r')
s= ""
for line in f1:
    s+=line
f1.close()
f2 = open('../samples/pythonstring2.txt', 'r')
s2= ""
for line in f2:
    s2+=line
f2.close()
# SF: calculate the number of comma-separated items
list1 = s.split(",")
list2 = s2.split(",");
print(len(list1))
print(len(list2))
# SF: compare the two list sets
difference = list(set(list1).difference(set(list2)))
print (difference)

# SF: Reading content from one file and writing it into another:
f = open('../samples/pythonstring2.txt', 'r')
output = open('../samples/pythonstring3.txt', 'w')
for line in f:
    output.write(line.rstrip() + '\n')
f.close()