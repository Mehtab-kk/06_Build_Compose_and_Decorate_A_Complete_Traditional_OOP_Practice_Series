class Logger:
    def __init__(self, name):
        self.name = name
        print(f"Logger object '{self.name}' created.")  # Constructor message

    def __del__(self):
        print(f"Logger object '{self.name}' destroyed.")  # Destructor message


def test():
    print("--- Start of scope ---")
    logger = Logger("TestLogger")  # Constructor runs
    print("--- End of scope ---")


test()  
import gc
gc.collect()