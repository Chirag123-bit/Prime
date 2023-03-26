#Python program to interchange first and last elements in a list
arr = [10,26,83,14,85]

# temp = arr[0] #Temporiarily store value of 1st item
# arr[0] = arr[-1] #Replace value of 1st item to last
# arr[-1] = temp #Replace value of last item to 1st

# arr[0], arr[-1] = arr[-1], arr[0]
# print(arr)


# Python program to swap two elements in a list
# arr[1], arr[2] = arr[2], arr[1]
# print(arr)


# Reversing the list
# lst = [1,2,3,4,5,6]
# reversed_array = []

# for i in range(len(lst)-1,-1,-1):
#     reversed_array.append(lst[i])

# print(reversed_array)

# lst = [1,2,3,4,5,6]
# start = 0
# end = len(lst)-1

# while end>start:
#     lst[start], lst[end] = lst[end], lst[start]
#     start +=1
#     end -=1
# print(lst)


# Occurence of a element in list

# arr = ["a","a", "a", "b", "b","a", "e", "e","e"]
# occs = {}
# for i in arr:
#     if(i in occs):
#         occs[i] +=1
#     else:
#         occs[i] = 1
# print(occs)


# Find largest element in list

arr = [10,32,878787,3434,5454,767676,878786,5534324]
arr2 = [10,11,2312,3412,3213,1241,24]


def secLargest(arr):
    largest = -1
    sec_largest = -1
    for i in arr:
        if(i>sec_largest):
            sec_largest = i
        if(sec_largest>largest):
            largest, sec_largest = sec_largest, largest

    print(sec_largest)



secLargest(arr)

secLargest(arr2)
