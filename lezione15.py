class FileMenager:

    def __init__(self,file_name: str, mode: str) -> None:

        self.file: str = file_name
        self.mode: str = mode

    def __enter__(self):
        self.file_wrapper = open(self.file_name, self.mode)

        return self.file_wrapper
    
    def __exit__(self, exp_type, exc_value, traceback):

        self.file_wrapper.close()

with FileMenager(file_name="prova.txt", mode="w") as file:

    file.write("Ciao")      

"""
Python integrated method

with open("prova.txt", "a") as file:
    file.write("Ciao")   
"""    


class Timer:

    def __enter__(self):
        import time
        self.time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        import time

        print(f"Time passed: {time.time() -  self.time}")
        return False
