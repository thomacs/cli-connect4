
def get_input(desired_type: type, variable: str = ""):
    """Function to get an user input of a given type"""

    while True:
        try:
            in_str: str = input()   
            out = desired_type(in_str)
            break
        except Exception as e:
            print(f"'{in_str}' is not a vaild input{f" for {variable}" if variable else ""}, please enter a(n) {desired_type.__name__}:")
            continue

    return out

    


    