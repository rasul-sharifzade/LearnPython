def findmax(r,k,y):
   if r < k < y:
       print(y)
   elif r < y < k:
       print(k)
   elif y < k < r:
       print(r)
   elif y < r < k:
       print(k)
   elif k < y < r:
       print(r)
   elif k < r < y:
       print(y)

print('findmax')

findmax(2,4,6)
findmax(2,6,4)
findmax(4,6,2)
findmax(4,2,6)
findmax(6,2,4)
findmax(6,4,2)

def findmax2(r,k,y):
    if r> k and r>y:
        print(r)
    elif k> r and k>y:
        print(k)
    else :
        print(y)

print('findmax 2')

findmax2(2,4,6)
findmax2(2,6,4)
findmax2(4,6,2)
findmax2(4,2,6)
findmax2(6,2,4)
findmax2(6,4,2)