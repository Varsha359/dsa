#Code 1
def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    total = sum(arr)
    minimum = total -arr[len(arr)-1]
    maximum = total-arr[0]
    print(minimum,maximum)

#Code 2
def miniMaxSum(arr):
    print(sum(arr) - max(arr), sum(arr) - min(arr))

#Code 3
def miniMaxSum(arr):
  arr.sort()
  print(sum(arr[0:-1]),sum(arr[1:]))
