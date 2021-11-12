with open ("customers.csv") as customer_data:
    line_counter = 0
    customer_list = []
    data_header = []
    while 1:
        data = customer_data.readline()
        if not data: break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            customer_list.append(data.split(","))
        line_counter += 1
print("Header : \t", data_header)
for i in range(0, 10):
    print("Data", i, ":\t\t", customer_list[i])
print(len(customer_list))