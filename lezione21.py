class Analisi:
    
    @staticmethod

    def tempo(func):
        def toni(*args):   #warpped = toni = any name
            import time
            start = time.time()
            value = func(*args)
            print(f" Time elapsed: {time.time() -start}")
            return value, time.time() - start
        return toni

@Analisi.tempo
def area_cerchio(raggio: float):
    return raggio * raggio *3.14

area_cerchio(1)

############################################

def generatore():
    
    
    yield "A"
    yield "B"
    yield "C"

prova_generatore = generatore()

print(next(prova_generatore))
print(next(prova_generatore))
#####################################

import time
from contextlib import contextmanager
@contextmanager    
def context_menager_decorator():

    start_time: float = time.time()
    yield
    end_time: float = time.time()
    elapsed_time = end_time - start_time

    print(f"{elapsed_time}")

@context_menager_decorator
def area_cerchio(raggio: float):
    return raggio * raggio * 3.14

area_cerchio(2)    

#########################
import sys 
a = []
b = a
print(sys.getrefcount(b))
