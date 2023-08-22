"""1. WAP to check if the given contact number is valid or invalid using regular expressions-


(Summary: Different country has a different type of representation on how they write their contact numbers, and the same number can be written in all kinds of other formats, so you have to analyse if the given number is valid or not based on your understanding). Examples of different formats of numbers found on websites:

2124567890
212-456-7890
(212)456-7890
(212)-456-7890
212.456.7890
212 456 7890
+12124567890
+12124567890
+1 212.456.7890
+212-456-7890
1-212-456-7890


As we can see above these are all the same numbers written in a different format, but they all are valid numbers. If you cannot prove all of them to be valid numbers, hoping to have at least 5 of them correctly to pass this.

HINT: The standard format is - [+][country code][area code][local phone number]"""





'''import phonenumbers

def is_valid_contact_number(number):
    try:
        # Parse the input number using the phonenumbers library
        parsed_number = phonenumbers.parse(number, None)
        
        # Check if the parsed number is valid according to phonenumbers
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.NumberParseException:
        # If parsing fails (invalid format), return False
        return False

contact_number = input("Enter a contact number: ")
if is_valid_contact_number(contact_number):
    print(f"{contact_number} is a valid contact number.")
else:
    print(f"{contact_number} is an invalid contact number.")'''






import re

def is_valid_contact_number(contact_number):
    # Regular expression pattern for valid contact numbers in any format
    pattern = r'^(\+\d{0,2} ?\d{1,4}[-.\s]?)?[(]?\d{1,4}[)]?[-.\s]?\d{1,4}[-.\s]?\d{1,10}$'
    
    # Check if the contact number matches the pattern
    
    if re.match(pattern, contact_number):
        return True
    else:
        return False

number_formats = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890"
]

# Check each example number format
for number in number_formats:
    if is_valid_contact_number(number):
        print(f"'{number}' is a valid contact number")
    else:
        print(f"'{number}' is an invalid contact number")
        
        
        
        
        
        
        

