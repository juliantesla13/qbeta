#!/usr/bin/python

__author__ ="Julian Andres Gomez"
__copyright__ = "Copyright 2018, Qbeta"
__credits__ = "Qbeta"
__license__ = "Apache License 2.0"
__version__ = "1.0.1"
__maintainer__ = "Julian Andres Gomez"
__email__ = "juliantesla13@gmail.com"
__status__ = "Production"

import numpy as np
import math as mt
import cmath as cmt
 
def qbit():
    """create the two quantum states in the qbit function """
    Zero = np.array([[1.0],  [0.0]])
    One = np.array([[0.0],   [1.0]])
    return Zero, One

def NormState(state): 
    """normalize the states """
    return  state / np.linalg.norm(state)
   
def Hadamard():
    """gate of hardamard   """
    return 1./np.sqrt(2) * np.array([[1, 1], [1, -1]])

def NewState(p, q):
    """create a new state  """
    return np.dot(p, q)

def NKron(*args):
  """ Calculate a Kronecker product on a variable number of entries """
  result = np.array([[1.0]])
  for op in args:
    result =np.kron(result, op)
  return result

def kron(a, b):
    """ Calculate a Kronecker product on a pair of input variables """
    return np.kron(a, b)  

def gatex():
    """gate X"""
    return  np.array([[0,1], [1,0]])

def gatep0():
    """gate P0 """
    Zero = np.array([[1.0],  [0.0]])
    return np.dot(Zero, Zero.T)

def gatep1():
    """gate P1  """
    One = np.array([[0.0],  [1.0]])
    return  np.dot(One, One.T)

def gateR(theta):
    """ Phase shift doors"""
    return  np.array([[1,0], [0, cmt.exp( theta*1j )]])

def medirstate(qbits):
    """ measure the quantum state """
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

if  __name__=='__main__':

    #creation of the qbits
    Zero, One =qbit()
    #create the identity matrix
    Id = np.eye(2)
    x1=Zero
    #I define a quantum state
    Hx1=NewState(Hadamard(),x1)
    #quantum state measurement
    s=medirstate (Hx1)
    print (s)






    
