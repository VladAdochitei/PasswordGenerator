#Passwork - basic password generator#
import random

print('Welcome to Passwork')

charSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=_+[]{}'


#This input will represent the number of passwords that are to be generated
passwordNumber = input('Amount of passwords to generate: ')
#The input will be saved as string, the following command will convert it to an integer
passwordNumber = int(passwordNumber)
#This input represents the length of the passwords
passwordLength = input('Input your password length: ')
#-II-
passwordLength = int(passwordLength)

print('\nCreated passwords:')
#The output file is set to ~append~ meaning that the file will not be overwritten
file = open("passwords.txt","a")
for pwd in range(passwordNumber):
    passwords = ''
    for i in range(passwordLength):
        passwords += random.choice(charSet)
    print(passwords)
    file.write(passwords + '\n')
file.write('\n')
file.close()



