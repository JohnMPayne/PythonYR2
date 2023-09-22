n = int(input())
arr = map(int, input().split())


print(sorted(set(arr))[-2])

#this print statement sorts the arr variable from small to large and get the -2 index 
#for the second largest number in the whole list. 