"""
try:
    file = open("order.txt")
    print("File is now open")
except FileNotFoundError as errmsg: #set premade error message
    print("File cannot be found")
    print(errmsg)# print premade error message
    raise
"""


def open_and_print_file(file):
    try:
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.rstrip("\n"))
    except:
        print ("File not found")
        raise
    finally: 
        print("\nExecution complete")

#open_and_print_file("order.txt")


def write_to_file(file, order_item):
    try:
        with open(file, "w") as file:
            file.write(order_item + "\n")
    except:
        print ("File not found")
        raise

write_to_file("order.txt", "dddddd")

open_and_print_file("order.txt")


"""
        opened_file = open(file, "r")
        file_line_list = opened_file.readlines()
    
        for line in file_line_list:
            print(line.rstrip('\n'))

        opened_file.close()

    except FileNotFoundError:
        print("error")
        raise



"""
