import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
        
    raw_data = np.array(list)
    matrix = raw_data.reshape(3,3)
    mean = [
        np.mean(matrix, axis=0),
        np.mean(matrix, axis=1),
        np.mean(matrix)
    ]
    variance = [
        np.var(matrix, axis=0),
        np.var(matrix, axis=1),
        np.var(matrix)
    ]
    standard_deviation = [
        np.std(matrix, axis=0),
        np.std(matrix, axis=1),
        np.std(matrix),
    ]
    maximum = [
        np.max(matrix, axis=0),
        np.max(matrix, axis=1),
        np.max(matrix)
    ]
    minimum = [
        np.min(matrix, axis=0),
        np.min(matrix, axis=1),
        np.min(matrix),
    ]
    theSum = [
        np.sum(matrix, axis=0),
        np.sum(matrix, axis=1),
        np.sum(matrix)
    ]
    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': maximum,
        'min': minimum,
        'sum': theSum
    }
