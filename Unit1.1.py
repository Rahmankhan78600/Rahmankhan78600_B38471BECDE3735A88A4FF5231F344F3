i=1
fact=1
n=int(input("enter the number:"))
while(i<=n):
  fact=fact*i
  i=i+1
print(fact)  


year=int(input("enter the number:"))
if(year%4==0):
  print(year,"is leap year")
else:
  print(year,"non leap year")