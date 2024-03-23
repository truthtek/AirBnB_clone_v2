def do_create(self, arg):
    """
    Create a new instance of a class
    Usage: create <class_name> <param 1>=<value 1> <param 2>=<value 2> ...
    """
    args = parse_args(arg)
    if not args:
        print("** class name missing **")
        return

    class_name = args[0]
    if class_name not in HBNBCommand.classes:
        print("** class doesn't exist **")
        return

    new_obj = HBNBCommand.classes[class_name]()
    params = args[1:]
    for param in params:
        key, value = param.split("=", 1)
        if value.startswith('"'):
            value = value.strip('"').replace('_', ' ')
            if value.endswith('"'):
                value = value[:-1]
            else:
                print(f"** value for {key} is not a valid string **")
                continue
        elif "." in value:
            try:
                value = float(value)
            except ValueError:
                print(f"** value for {key} is not a valid float **")
                continue
        else:
            try:
                value = int(value)
            except ValueError:
                print(f"** value for {key} is not a valid integer **")
                continue

        setattr(new_obj, key, value)

    new_obj.save()
    print(new_obj.id)

def parse_args(arg):
    """
    Parse the arguments from the command line
    """
    args = arg.split()
    parsed_args = []
    for arg in args:
        if "=" in arg:
            parsed_args.append(arg)
        else:
            parsed_args.append(arg)
    return parsed_args
