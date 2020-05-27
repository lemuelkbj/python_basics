# Script for printing the common between the two lists, specific to the position of the item in the lists
# If list1 has an item '1' in 2nd position (i = 1) then list2 should have '1' in the same 2nd position
list1 = []  # emptylist
list2 = []
for i in range(0, int(input("Enter the range : "))):
    list1.append(input("Enter the %s item of the list 1: " % (i+1)))    # appending both lists simultaneously
    list2.append(input("Enter the %s item in list 2 : " % (i+1)))
count = 0
# minimizing our comparison of items by finding the minimum length among the lists
lt = min(len(list1), len(list2))
for i in range(lt):
    if list1[i] == list2[i]:
        print(list1[i], end=" ")
        count += 1
print("\n", count)
