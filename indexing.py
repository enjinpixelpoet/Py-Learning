# Indexing: Allows us to access elements of a sequence using []
# [Start:End:Step]

credit_number = "1234-2345-3456-4567"

# print(credit_number[0:4])
# print(credit_number[5:9])
# print(credit_number[10:14])
# print(credit_number[15:19])
# print(credit_number[20:24])
# print(credit_number[::1])

last_digits = credit_number[-4:]
print(f"Last 4 digits: {last_digits}") 

credit_number= credit_number[::-1]
print(credit_number)