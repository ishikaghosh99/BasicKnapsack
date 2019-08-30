#knapsack using greedy
from ass3 import Knapsack
from ass2 import Sorting1
from ass2 import Sorting2
from ass2 import Sorting3
   
w=[]
p=[]
r=[]
n=int(input("Please Enter the Total Number of Quantity : "))
for i in range(n):
    value = int(input("Please enter the %d Element of Weight array: " %i))
    w.append(value)
print("The weight array is as :",w)
for i in range(n):
    value1 = int(input("Please enter the %d Element of Profit array: " %i))
    p.append(value1)
print("The profit array is as :",p)
for i in range(n):
    value2=p[i]/w[i]
    r.append(value2)
print("The profit/weight array is as :",r)
capacity=int(input("Please Enter the Total Capacity : "))
print("Select the Operation You want to perform")
number=int(input("1.Minimum Weight 2.Maximum Profit 3.Maximum Profit/Weight Ratio"))
if(number==1):
    Sorting1(w,n,p)
if(number==2):
    Sorting2(w,n,p)
if(number==3):
    Sorting3(w,n,p,r)
ans=Knapsack(w,p,capacity,n)
print("The total profit obtained is:",ans)
