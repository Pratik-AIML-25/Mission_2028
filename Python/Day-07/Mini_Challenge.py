'''
Password Login using Functions

Correct Password
python2028

If correct
Welcome User

Else
Access Denied

Use a function to check the password.                                                                                                    '''


# CODE

# Function to check password
def check_password(password):
    if password == "python2028":
        return "Welcome User"
    else:
        return "Access Denied"

# Main Program
password = input("Enter Password: ")

# Function Call
result = check_password(password)

# Output
print(result)