import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    #e = 1+np.exp(-x)
    x = np.asarray(x)
    sig = 1 / (1+ np.exp(-x))
    return sig
    #pass