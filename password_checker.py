import re

# Function to check the strength of a password
def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Password should be at least 8 characters long."
    
    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        return "Password should contain at least one uppercase letter."
    
    # Check for numbers
    if not re.search(r'[0-9]', password):
        return "Password should contain at least one number."
    
    # Check for special characters
    if not re.search(r'[@#$%^&+=!]', password):
        return "Password should contain at least one special character (@, #, $, %, ^, &, +, =, or !)."
    
    # If all conditions are met, password is strong
    return "Password is strong."

# Main function to take user input
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)

