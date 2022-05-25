import random

p = random.randint(10,100)
x = str(p)+"\n"
for i in range(p):
    x += str(random.randint(10,100))
    if(i!=p-1):
        x += "\n"
inputfile = 'input000.txt'
f = open(inputfile,'w')
f.write(x)
f.close()
f = open(inputfile, 'r')
x = int(f.readline())
arr = []
for i in range(x):
    arr.append(int(f.readline()))

def search(n,li):
    a = [0]*(n-1)
    a[n-2] = li[n-1]
    for i in range(n-3,-1,-1):
        a[i] = a[i+1]|li[i+1]
    b = [0]*(n-1)
    for i in range(n-1):
        b[i] = a[i]^li[i]
    ans = b[0]
    for i in range(1,n-1):
        ans |= b[i]
    return ans
   

   

# logic
count = search(x, arr)

# store output in count variable and in string format

f.close()
f = open('output009.txt', 'w')
f.write(str(count))
f.close()