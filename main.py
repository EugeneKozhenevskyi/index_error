def check_index_error():
    try:
        my_list = [1, 2, 3, 4]
        print(my_list[6])
    except IndexError:
        print("Error: Index not found")
    finally:
        print("Check end")


check_index_error()
