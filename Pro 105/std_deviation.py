import math 
import csv
with open('data1.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

#find mean
def mean(data):
    n = len(data)
    total= 0
    for x in data:
        total += int(x)
    
    mean = total/n
    return mean

#subtract the mean from values and square
squared_list = []

for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared_list.append(a)

#get sum
sum = 0
for i in squared_list:
    sum += i

#divide by total value - 1
result = sum/(len(data)-1)
#sqroot of the result
std_deviation= math.sqrt(result)
print(std_deviation)

