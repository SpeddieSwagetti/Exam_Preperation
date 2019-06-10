value = int(0)
sequence_list = []
for element in range(0, 15, 3):
    value += element
    if element < 10:
        element = "0{}".format(element)
    else:
        element = str(element)
    sequence_list.append(element)
print(sequence_list)

l1 = ["eat", "sleep", "repeat"]
obj1 = enumerate(l1)
print(list(obj1))

for element in enumerate(l1, 100):
    print(element)