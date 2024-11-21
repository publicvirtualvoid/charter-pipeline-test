import numpy as np
from scipy import stats

def calculate(numbers):
    """
    Calculate various statistics for a given list of numbers.
    
    Args:
    numbers (list): A list of numbers to analyze.
    
    Returns:
    dict: A dictionary containing calculated statistics.
    """
    if not numbers:
        return {"error": "Empty input list"}
    
    try:
        numbers = [float(num) for num in numbers]
    except ValueError:
        return {"error": "Invalid input. All elements must be numbers."}
    
    results = {
        "mean": np.mean(numbers),
        "median": np.median(numbers),
        "std_dev": np.std(numbers),
        "variance": np.var(numbers),
        "skewness": stats.skew(numbers),
        "kurtosis": stats.kurtosis(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }
    
    return results