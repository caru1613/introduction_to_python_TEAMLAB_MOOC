while True:
    value = input("Input values to convert: ")
    for digit in value:
        if digit not in "0123456789":
            raise ValueError("integer is not included.")
    print("Integer value: ", int(value))