import numpy as np
import math as mt
import cmath as cmt
 
#crear los dos estados cuantico en la funcion qbit

def qbit():
    Zero = np.array([[1.0],  [0.0]])
    One = np.array([[0.0],   [1.0]])
    return Zero, One

# normalizar los estados 
def NormState(state): 
    return  state / np.linalg.norm(state)

    
    
# compuerta de hardamard    
def Hadamard():
    return 1./np.sqrt(2) * np.array([[1, 1], [1, -1]])

#crear un nuevo estado 
def NewState(p, q):
    return np.dot(p, q)

# Calcular un producto Kronecker sobre un número variable de entradas
def NKron(*args):
  result = np.array([[1.0]])
  for op in args:
    result =np.kron(result, op)
  return result

# Calcular un producto Kronecker sobre un par de variables de entradas
def kron(a, b):
    return np.kron(a, b)  

#compuerta X
def gatex():
    return  np.array([[0,1], [1,0]])

#compuerta P0
def gatep0():
    Zero = np.array([[1.0],  [0.0]])
    return np.dot(Zero, Zero.T)

#compuerta P1   
def gatep1():
    One = np.array([[0.0],  [1.0]])
    return  np.dot(One, One.T)

#Puertas de desplazamiento de fase
def gateR(theta):
    return  np.array([[1,0], [0, cmt.exp( theta*1j )]])

# medir el estado cuantico 
def medirstate(qbits):
    nqbits =NormState(qbits)
    qbits = np.dot(nqbits, nqbits.T)
    P0= gatep0()
    b=int (mt.log(qbits.shape[0],2))
    if b==1 :
        Prob0 = np.trace(np.dot(P0, qbits))
        return Prob0.real

    result =np.kron(P0, Id)
  
    for x in range(2, b):
        result =np.kron(result, Id)
    Prob0 = np.trace(np.dot(result, qbits))    
    
    return Prob0.real

#cuerpo del progrma

def main():
    #creacion de los qbits
    Zero, One =qbit()
    #crea la matriz identidad
    Id = np.eye(2)
    x1=Zero
    #defino un estado cuantico 
    Hx1=NewState(Hadamard(),x1)
    #medicion del estado cuantico 
    s=medirstate (Hx1)
    print (s)
    return 0

# funcion de inicio
main()




    
