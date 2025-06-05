

def is_playing():
    from ..__init__ import is_loaded
    if is_loaded:
        print("Module1 is loaded successfully!")
    else:
        print("Module1 is not loaded successfully!")
    print(is_playing.__module__, "running the plays...!")
    