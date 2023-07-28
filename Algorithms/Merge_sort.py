import math

# Merge Sort Implementation
# Reference -> https://www.youtube.com/watch?v=HrCPqJHQSxY&t=615s&ab_channel=KantanCoding

def merge(leftArr, rightArr):
    leftArrIndex = 0
    rightArrIndex = 0

    sortedArr = []

    while ((leftArrIndex < len(leftArr)) and (rightArrIndex < len(rightArr))):
        if leftArr[leftArrIndex] >= rightArr[rightArrIndex]:
            sortedArr.append(rightArr[rightArrIndex])
            rightArrIndex += 1
        else:
            sortedArr.append(leftArr[leftArrIndex])
            leftArrIndex += 1

    # option 1
    sortedArr.extend(leftArr[leftArrIndex:])
    sortedArr.extend(rightArr[rightArrIndex:])
    return sortedArr
    # OR
    # # option 2
    # # "slice" method can be used for below
    # return sortedArr + leftArr[leftArrIndex:len(leftArr)] + rightArr[rightArrIndex:len(rightArr)]


def mergeSort(arr):

    if len(arr)<=1:
        return arr


    middleIndex = math.floor(len(arr)/2)
    leftArr =  arr[:middleIndex]
    rightArr = arr[middleIndex:]


    return merge(mergeSort(leftArr),mergeSort(rightArr))

print(mergeSort([6,1,23,3,0]))