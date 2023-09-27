x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))

# these loop statements iterate over a range of numbers starting from 0 and ending at x y and z
# inclusive. Then ending of this statement makes sure that the addition of i, j and k are not equal to 0. 