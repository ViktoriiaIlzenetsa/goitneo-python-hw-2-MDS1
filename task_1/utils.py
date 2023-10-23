def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error! Name not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name"
        
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Such a contact with this name already exists. Contact updated"
    else:
        contacts[name] = phone
        return "Contact added."
    
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error! Name not found."
    
@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]
  

def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")



if __name__ == "__main__":
    pass