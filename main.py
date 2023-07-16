import string #IMPORTING THE STRING MODULE
import random 

if __name__ == '__main__': 
    def password_generator():
        while True:
            string1 = string.ascii_lowercase
            string2 = string.ascii_uppercase
            string3 = string.digits
            string4 = string.punctuation

            password_list = [] #ADDING THE LETTERS,DIGITS AND PUNCTUATION TO LIST
            password_list.extend(string1)
            password_list.extend(string2)
            password_list.extend(string3)
            password_list.extend(string4)
            # print(password_list)

            password_lenght = input('Enter the lenght of password or press q to quit: ')
            if password_lenght == 'q':  #TO EXIT THE PROGRAM
                print('Thanks for using this program!!')
                break
            else:
                try: #HANDLING THE EXCEPTION
                    password_lenght = int(password_lenght)
                    random.shuffle(password_list)
                    # print(password_list)
                    # password=''.join(random.sample(password_list,password_lenght))    -->Another     method
                    password = ''.join(password_list[0:password_lenght])
                    print(f'Your new password is {password}')
                except Exception as e:
                    print("Please enter a valid number.")

password_generator() #CALLING THE FUNCTION
