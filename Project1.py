#Q1
# list with 5 integers, 5 floats, and 5 strings
mylist = [10, 25, -3, 42, 7, 3.14, 2.71, -1.0, 0.0, 9.8, "apple", "banana", "cat", "hello", "python"]
print(mylist)


#Q2
# yes it does

mylist.append(4)
mylist.append(5.2)
mylist.append('gvei')
print(mylist)

#Q3
# ofc

# Create an empty list
mylist2 = []

# Insert items into the list
mylist2.insert(0, 'Hello')  # insert at index 0
mylist2.insert(1, 'Gvei')  # insert at index 1
mylist2.insert(2, 'Ppl')   # insert at index 2

print(mylist2)  # Print the updated list

#Q4

for i in mylist:
  print(i)

#Q5

mylist3 = [34, 12, 5, 67, 23, 89, 2, 45, 10, 78]
# ascending
ascendingmylist3 = sorted(mylist3)
print(ascendingmylist3)
descendingmylist3 = sorted(mylist3, reverse=True)
print(descendingmylist3)

#Q6
mylist4 = ["hello", "gvei", "Mueed", "MehrajSir", "Computer", "Science", "Gold", "plate", "noir", "tier"]

ascendingmylist4 = sorted(mylist4)
descendingmylist4 = sorted(mylist4, reverse=True)
print(ascendingmylist4)
print(descendingmylist4)

#Q7

mylist5 = []

mylist5.insert(1, 7)
mylist5.insert(2, 8)
mylist5.insert(3, 6)
print(mylist5)

#Q8

mylist6 = [1,4,2,5,3,27362,5,4,4, 30,2222,33,31184,35,4,34,3,4,72727234,34]
print(max(mylist6))
print(min(mylist6))

#Q9

mylist7 = [1, 3, 4,2,2,4,2,2,3,4,4,3,3]
sublist1 = [1,8,9]
sublist2 = ["a", "b", "c"]
mylist7.append(sublist1)
mylist7.append(sublist2)
print(mylist7)

mylist8 = [1,2,5,3,5,3,3,5,7,7,8,8,9,3,2,5,6,9]
mylist8.append(78)
mylist8.insert(3, 999)
mylist8.remove(5)
mylist8.pop(3)
mylist8.copy()
print(mylist8)