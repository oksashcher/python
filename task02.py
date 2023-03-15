#n = int(input())
#c = n % 10
#n = n// 10
#b = n %10
#a = n//10
#print (a + b + c)


#s = int(input())
#a = (s//6)
#b = ((s//6)*4)
#c = (s//6)
#print (a), (b), (c) 



#ticket = int(input())
#sum1 = ticket[0] + ticket[1] + ticket[2]
#sum1 = ticket[3] + ticket[4] + ticket[5]
#if sum1 == sum2:
#    print("yes")
#else:    
#    print("no")


n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("yes")
else:
    print ("no")
        




