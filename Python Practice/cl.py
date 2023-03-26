# num = input("Enter a number: ")
# num2 = input("Enter a number: ")

# try:
#     num = int(num)
#     num2 = int(num2)
#     print(num/num2)

# except ValueError:
#     print("Value Error....Please Enter NUMBERS")

# except ZeroDivisionError:
#     print("Cannot Divide By Zero")


# finally:
#     print("Finally It ends here")




def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    while(low<=high):
        mid = (low+high)//2

        if(arr[mid]>x):
            high = mid-1

        elif(arr[mid]<x):
            low = mid+1

        elif(arr[mid]==x):
            return mid
    return -1



arr = [1,2,3,4,5]
x = -9

res = binary_search(arr,x)
print(res)

