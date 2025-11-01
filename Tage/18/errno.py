import errno

# file = open("nicht_da.txt")

for i in range(1, 41):
    error_number = i
    error_name = errno.errorcode[error_number]
    print(f"Error number {error_number:>2} corresponds to {error_name}")

errno_constants = [name for name in dir(errno) if name.isupper()]
print(errno_constants)