x , y , z , w = 12 , 2 , 14 , 7
if (w > x) and (w > y) and (w > z):
    print ("greatest number is" , w)
elif (x > w) and (x > y) and (x > z):
    print ("greatest number is" , x)
elif (y > w) and (y > x) and (y > z):
    print ("greatest number is" , y)
elif (z > w) and (z > x) and (z > y):
    print ("greatest number is" , z)


n = 15
count = 0
q = 2**n
while q != 0:
    count += q%10
    q = q//10
print(count)