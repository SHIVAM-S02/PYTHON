n=int(input("Enter the number of elements to be inserted"))
a=[]
for i in range(0,n):
    elem=int(input("Enter Element:"))
    a.append(elem)
avg=sum(a)/n
print("Average of the elements in the list",round(avg,2))