import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email=input("Enter an email address to encrypt")):
    """
    cipher.py: encrypts and decrypts email addresses
    created by: christine roe
    course number: csc138 en
    created on: 092824
    
    Objective is to encrypt and decrypt an email address that is input by the user. 
    The arguments can be any letter from a to z and any number from 0 to 9. Data
    types are string and integer but the integers will be turned into a string. 
    The variables are the encrypted and decrypted email addresses. Data type string. 
    """
    output = "" 
    len_flag = len(email) != 6
    # Makes sure first 3 characters are alpha and last 3 characters are digit 
    # keep all updates in the anum_flag (bool) variable
    anum_flag = not (email[:3].isalpha() and email[3:].isdigit()) 

    if len_flag:                         # Lengh validation
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # Alpha/digit validation
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     
        
    # Processes string into a list
    email_lst = list(email)
        
    new_ascii = ord(email_lst[0]) + 3    # NOTE: here we extract and update element at 0 
    email_lst[0] = chr(new_ascii)        # NOTE: here we convert our ASCII into string
    #Separates alphas and digits and shifts each up 3 
    for i in range(len(email_lst)):    
        if email_lst[i].isalpha():
            email_lst[i] = chr(ord(email_lst[i]) + 3)
        elif email_lst[i].isdigit():
            email_lst[i] = str((int(email_lst[i]) + 3))    
     # Converts the elements into a string
    str(email_lst) 
    # Converts list into a string
    email_str = ''.join(map(str, email_lst))

    # keep all updates in the retVal (str) variablei
    retVal = email_str
    return retVal 

def decrypt(email):
    """
    The objective is to decrypt an email address. 
    The arguments can be any letter from a to z and any number from 0 to 9 
        and the data type is string.
    The variable being returned is dec email. The data type would be string.    
    """
    # input validation
    output = "" 
    len_flag = len(email) != 6
    # keep all updates in the anum_flag (bool) variable
    
    anum_flag = not (email[:3].isalpha() and email[3:].isdigit())

    if len_flag:                         # Lengh validation
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # Alpha/digit validation
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output 
        
    # Processes string into a list
    email_lst = list(email)
    # Separates alphas and digits and shifts down 3 
    for i in range(len(email_lst)):
        if email_lst[i].isalpha():
            email_lst[i] = chr(ord(email_lst[i]) - 3)
        elif email_lst[i].isdigit():
            email_lst[i] = str((int(email_lst[i]) - 3))        
    # Converts list into a string
    email_str = ''.join(map(str, email_lst))

    retval = email_str
    return retVal
