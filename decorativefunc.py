def outer_function(f):
    def wrapper(*args, **kwrags):
        #kwarg takes single value at a time
        # **kwargs takes dict as input format
        #*arg takes input ad list format
        res = f(*args, **kwrags)
        if isinstance(res, dict):
            print("checked that the input is a dictionary")
            return res
    return wrapper

@outer_function
def give_dictionary(arg):
    return {"program": arg}

print(give_dictionary("python"))