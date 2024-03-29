from functionality import get_all_items, pretty_output, get_a_chain


# menu
greeting_string = """
    Hello there. Please select an option:
    1. Get all items of a specific type
    2. Get all related items
"""
print(greeting_string)
option = input("> ")

match option.strip():
    case '1':
        print("Select type of the items you want to see:\n1. seeds\n2. crops\n3. animals\n4. animal prodcuts")
        type_selected = input("> ")
        res = get_all_items(type_selected)
        pretty_output(res)

    case '2':
        print("Select type of the items you want to see:\n1. seeds\n2. crops\n3. animals\n4. animal prodcuts")
        type_selected = input("> ").strip()
        print("enter th name of the item")
        item_name = input("> ").strip()
        res = get_a_chain(type_selected, item_name)
        print(res)

