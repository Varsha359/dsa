def twoSum(arr, target, n):
    # Write your code here.
    hashmap = {}
    ans = []

    hashmap = {}
    ans = []
    for i in range(n):
        #intializing the hashmap
        if arr[i] not in hashmap:
            hashmap[arr[i]]=1
        else:
            hashmap[arr[i]]+=1
        #check if b present in hashmap
        #if not continue for next iteration
        if target-arr[i] not in hashmap:
            continue
        #if there, if a==b then check freq
        if target-arr[i] == arr[i]:
            if hashmap[arr[i]]>1:
                ans.append([arr[i],arr[i]])
                hashmap[arr[i]]-=2
            
        else:
            if hashmap[arr[i]]>0 and hashmap[target-arr[i]]>0:
                ans.append([arr[i],target-arr[i]])
                hashmap[arr[i]]-=1
                hashmap[target-arr[i]]-=1
    if len(ans)==0:
        ans.append([-1,-1])
    return ans

def takeInput() :

    n, tar = map(int, input().strip().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    return n, tar, arr

def printAns(ans):
    for i in ans:
        if i[0] < i[1]:
            print('{} {}'.format(i[0], i[1]))
        else:
            print('{} {}'.format(i[1], i[0]))

t = int(input().strip())
for i in range(t) :

    n, target, arr = takeInput()

    ans = twoSum(arr, target, n)
    printAns(ans)
