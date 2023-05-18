import random, time

def linear_search(lst, target):
    for val in range(len(lst)):
        if lst[val]==target:
            return 1
    return -1

def binary_search(lst, target, low=None, high=None):

    if low is None:
        low=0
    if high is None:
        high=len(lst)-1
    if high<low:
        return -1

    mid=(low+high)//2

    if lst[mid]==target:
        return mid
    elif target<lst[mid]:
        return binary_search(lst, target, low, mid-1)
    else:
        return binary_search(lst, target, mid+1, high)

if __name__=="__main__":

    # lst=[1,3,5,7,11,13,17,19]
    # target=7
    # print(linear_search(lst, target))
    # print(binary_search(lst, target))

    length=1000
    sorted_list=set()
    while(len(sorted_list)<length):
        sorted_list.add(random.randint(-1*length, 1*length))
    sorted_list=sorted(list(sorted_list))

    start=time.time()
    for target in sorted_list:
        linear_search(sorted_list, target)
    end=time.time()
    timeDiff=end-start
    print(f"Time taken for linear search {timeDiff}")

    start=time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end=time.time()
    timeDiff=end-start
    print(f"Time taken for binary search {timeDiff}")