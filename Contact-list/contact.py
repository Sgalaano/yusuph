import pyperclip
class Contact:
    """
    Class that generates new instances of contacts.
    """

    contact_list = [] # Empty contact list

    def __init__(self,first_name,last_name,number,email):

        # docstring removed for simplicity

            self.first_name = first_name
            self.last_name = last_name
            self.phone_number = number
            self.email = email

    contact_list = [] # Empty contact list
    # Init method up here
    def save_contact(self):

            '''
            save_contact method saves contact objects into contact_list
            '''

            Contact.contact_list.append(self)

    def delete_contact(self):

            '''
            delete_contact method deletes a saved contact from the contact_list
            '''

            Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls,number):

            '''
            Method that takes in a number and returns a contact that matches that number.

            Args:
            number: Phone number to search for
            Returns :
            Contact of person that matches the number.
            '''

            for contact in cls.contact_list:
                if contact.phone_number == number:
                    return contact

    @classmethod
    def contact_exist(cls,number):
            '''
            Method that checks if a contact exists from the contact list.
            Args:
            number: Phone number to search if it exists
            Returns :
            Boolean: True or false depending if the contact exists
            '''
            for contact in cls.contact_list:
                if contact.phone_number == number:
                        return True

            return False
    @classmethod
    def display_contacts(cls):
            '''
            method that returns the contact list
            '''
            return cls.contact_list


    @classmethod
    def copy_email(cls,number):
            contact_found = Contact.find_by_number(number)
            pyperclip.copy(contact_found.email)
            
def main():
                print("Hello Welcome to your contact list. What is your name?")  
                user_name = input()

                print(f"Hello {user_name}. what would you like to do?")
                print('\n')

                while True:
                                print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                                short_code = input().lower()

                                if short_code == 'cc':
                                        print("New Contact")
                                        print("-"*10)

                                        print ("First name ....")
                                        f_name = input()

                                        print("Last name ...")
                                        l_name = input()

                                        print("Phone number ...")
                                        p_number = input()

                                        print("Email address ...")
                                        e_address = input()


                                        save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
                                        print ('\n')
                                        print(f"New Contact {f_name} {l_name} created")
                                        print ('\n')

                                elif short_code == 'dc':

                                        if display_contacts():
                                                print("Here is a list of all your contacts")
                                                print('\n')

                                                for contact in display_contacts():
                                                        print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                                                print('\n')
                                        else:
                                                print('\n')
                                                print("You dont seem to have any contacts saved yet")
                                                print('\n')

                                elif short_code == 'fc':

                                        print("Enter the number you want to search for")

                                        search_number = input()
                                        if check_existing_contacts(search_number):
                                                search_contact = find_contact(search_number)
                                                print(f"{search_contact.first_name} {search_contact.last_name}")
                                                print('-' * 20)

                                                print(f"Phone number.......{search_contact.phone_number}")
                                                print(f"Email address.......{search_contact.email}")
                                        else:
                                                print("That contact does not exist")

                                elif short_code == "ex":
                                        print("Bye .......")
                                        break
                                else:
                                        print("I really didn't get that. Please use the short codes")
