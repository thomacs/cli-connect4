
def get_input(prompt: str, desired_type: type, variable: str = ""):
    """Function to get an user input of a given type"""
    print(prompt)

    while True:
        try:
            in_str: str = input()   
            out = desired_type(in_str)
            break
        except ValueError:
            print(f"\033[1A\033[2K\033[1A'{in_str}' is not a valid input{f" for {variable}" if variable else ""}, please enter valid {desired_type.__name__}:")
            continue

    return out


    


    