def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "User not found"
        except IndexError:
            return "Enter user name"
        except Exception:
            return "Please enter right command"

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def validate_args(args):
    if len(args) != 2 or not args[1].isdigit():
        return False
    return True


@input_error
def add_contact(args, contacts):
    if not validate_args(args):
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if not validate_args(args):
        raise ValueError
    name, phone = args
    if name not in contacts:
        return 'Contact is not found.'
    contacts[name] = phone
    return 'Contact is updated.'


@input_error
def show_contact(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name not in contacts:
        return 'Contact is not found.'

    return contacts[name]


@input_error
def show_all(args, contacts):
    contact_book = list()
    if len(args) != 0:
        raise Exception

    if contacts == {}:
        return "You don't have any contacts yet."
    for name, phone in contacts.items():
        contact_book.append('|{:>15} : {:<17}|'.format(name, phone))
    return "\n".join(contact_book)
