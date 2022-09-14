num_1 = int(input("Enter your first integer number: "))
num_2 = int(input("Enter your second integer number: "))
num_3 = int(input("Enter your third integer number: "))

total_operation_1 = None
total_operation_2 = None
total_operation_3 = None
total_operation_4 = None
total_operation_5 = None

total_operation_1 = num_1 - num_2
total_operation_2 = num_1 + num_2
total_operation_3 = num_1 * num_2
total_operation_4 = num_1 ** num_2
total_operation_5 = num_1 / num_2

print("Minus operation result is:",total_operation_1)
print("Sum operation result is:", total_operation_2)
print("Multiplication operation result is:", total_operation_3)
print("Power operation result is:", total_operation_4)
print("Division operation result is:", total_operation_5)

total_operation_1 = total_operation_1+num_3
total_operation_2 = total_operation_2-num_3
total_operation_3 = total_operation_3*num_3
total_operation_4 = total_operation_4**num_3
total_operation_5 = total_operation_5/num_3

print("Minus operation result is:",total_operation_1)
print("Sum operation result is:", total_operation_2)
print("Multiplication operation result is:", total_operation_3)
print("Power operation result is:", total_operation_4)
print("Division operation result is:", total_operation_5)
