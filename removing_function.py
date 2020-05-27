# lists the even numbers
def show_even(my_list):
    for numbers in my_list:  # iterate through the list
        if int(numbers) % 2 == 0:   # select the numbers which are even
            print("\n", numbers, end=" ")   # print it
            # Also if you want the numbers as a list just append it to an empty list


# create an empty list
mylist1 = []
for i in range(0, int(input("Enter the range :"))):
    mylist1.append(input("Enter the input : "))
# print the list
print(mylist1)
# direct the lists to the function
show_even(mylist1)
