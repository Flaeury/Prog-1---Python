import re


def very_strong(password):
    if len(password) >= 10 and\
            re.search("[A-Z]", password) and\
            re.search("[a-z]", password) and\
            re.search("[0-9]", password) and\
            len(re.findall("[@#$%&*+]", password)) >= 3:
        return True
    else:
        return False


def strong(password):
    if len(password) >= 8 and\
            re.search("[A-Z]", password) and\
            re.search("[a-z]", password) and\
            re.search("[0-9]", password) and\
            len(re.findall("[@#$%&*+]", password)) >= 1:
        return True
    else:
        return False


def medium(password):
    if len(password) >= 6 and\
            re.search("[A-Z]", password) and\
            re.search("[a-z]", password) and\
            re.search("[0-9]", password):
        return True
    else:
        return False


def weak(password):
    if len(password) >= 6 and\
            re.search("[^A-Z]", password) and\
            re.search("[^0-9]", password):
        return True
    else:
        return False


def none(password):
    if len(password) < 5 and\
            re.search("[^A-Z]", password) and\
            re.search("[^0-9]", password):
        return True

    elif len(re.findall("[0-9]", password)) > 1 and\
            re.search("[^a-z]", password):
        return True
    else:
        return False


def main():
    password = input("Digite uma senha: ")
    if very_strong(password) == True:
        print("Sua senha é muito forte!")
    elif strong(password) == True:
        print("Sua senha é forte!")
    elif medium(password) == True:
        print("Sua senha é média!")
    elif weak(password) == True:
        print("Sua senha é muito fraca!")
    elif none(password) == True:
        print("Isso não é uma senha!")

    return main()


def chamar():
    main()


chamar()           
