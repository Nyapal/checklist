checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    print(checklist[index])

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    print ("√ " + checklist[index])

def user_input(prompt):
    return input(prompt)

def select(function_code):
    if function_code == "C" or "c":
        input_item = user_input("Input Item: ")
        create(input_item)

    elif function_code == "R" or "r":
        item_index = user_input("Index Number? ")
        read(int(item_index))

    elif function_code == "U" or "u":
        item_index = user_input("Index Number? ")
        input_item = user_input("Update Item: ")
        update(int(item_index), input_item)

    elif function_code == "D" or "d":
        item_index = user_input("Index Number? ")
        destroy(int(item_index))

    elif function_code == "P" or "p":
        list_all_items()

    elif function_code == "Q" or "q":
        return False

    else:
        print("Unknown Option")

    return True

def test():

    create('go to gym')
    create('buy socks')
    create('return library book')
    create('clean bathroom')

    print(read(2))

    update(1, 'buy house slippers')

    list_all_items()

    destroy(3)

    list_all_items()

    mark_completed(1)

    test()

running = True
while running:
    selection = user_input ("Press C to add to list, R to Read from list, U to update list item, D to delete list item, P to display list, and Q to quit ")
    running = select(selection)
