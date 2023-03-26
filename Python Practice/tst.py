# Occurence of a element in list
arr = [11,1,1,1,2,2,3,4,4,4,5,5,3,1,2,3]
counter={}
for i in arr:
    if i in counter:
        counter[i] +=1
    else:
        counter[i]=1
print(counter)

# Find Second largest element in list
arr2 = [111,1,223,132131,12,32323,12213,34343,4545,454546,454546,65,75,75,7,575,64,4,54,5]
largest = -1
sec_largest = -2
for i in arr2:
    if(i>sec_largest and i!=largest):
        sec_largest = i
    if(sec_largest>largest):
        largest,sec_largest = sec_largest,largest
print(sec_largest)


# Print unique items in a list
unique_items = set(arr)
unique_items =  list(unique_items)
print(unique_items)



#Linear Method
arr3 = [1,2,3,4,5,6,7,8]
itemToFind = 5
found = False
index = -1

for i in range(len(arr3)):
    if(arr3[i]==itemToFind):
        found= True
        index = i
        break
    else:
        found = False
if(found):
    print(f"Item Found at index {index}")
else:
    print("Item Not Found")



#Binary Method


0