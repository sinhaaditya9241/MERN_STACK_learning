import numpy as np 

def generate_random_array(size):

    """
    Generates a random array of given size with values between 0 and 1.

    Parameters:
    size (int): The size of the array to generate.

    Returns:
    np.ndarray: An array of random floats.
    """
    return np.random.rand(size)