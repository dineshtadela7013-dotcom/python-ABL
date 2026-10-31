
password = input("Enter your password: ")

errors = []

if len(password) < 8:
    errors.append("Minimum 8 characters required")

if not any(ch.isupper() for ch in password):
    errors.append("One uppercase letter required")

if not any(ch.islower() for ch in password):
    errors.append("One lowercase letter required")

if not any(ch.isdigit() for ch in password):
    errors.append("One digit required")

if not any(not ch.isalnum() for ch in password):
    errors.append("One special character required")

print("\nPASSWORD VALIDATION RESULT")

if len(errors) == 0:
    print("Strong Password")
    print("Password Accepted")

else:
    print("Weak Password")
    print("Errors:")

    for error in errors:
        print("-", error)
