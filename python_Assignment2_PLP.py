my_list = []
print("Starting list:", my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After adding 10, 20, 30, 40:", my_list)

my_list.insert(1, 15)
print("After inserting 15 at position 2:", my_list)

my_list.extend([50, 60, 70])
print("After extending with [50, 60, 70]:", my_list)

removed_item = my_list.pop()
print(f"Removed the last item ({removed_item}):", my_list)

my_list.sort()
print("After sorting in ascending order:", my_list)

index_30 = my_list.index(30)
print("The value 30 is at index:", index_30)
