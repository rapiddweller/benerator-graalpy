import logging
import requests

# Setting up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def multiply(a, b):
    """
    Multiply two numbers.

    This function takes two arguments, `a` and `b`, which should be numbers (integers or floats).
    It returns the product of `a` and `b`.

    Parameters:
    a (int/float): First number
    b (int/float): Second number

    Returns:
    int/float: Product of `a` and `b`

    Raises:
    TypeError: If `a` or `b` is not a number.
    """
    try:
        # Type checking
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both arguments must be numbers")

        # The multiplication operation using a lambda function
        multiply_op = lambda x, y: x * y
        result = multiply_op(a, b)

        logging.info("Multiplication successful")
        return result
    except TypeError as e:
        logging.error(f"TypeError occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

def fetch_web_content(url):
    """
    Fetch content from a web URL using the 'requests' library in Python.
    Demonstrates the use of Python libraries in GraalVM.
    """

    response = requests.get(url)
    return response.text

def complex_operation_with_pandas(input_value):
    """
    Performs a complex operation on a DataFrame using Pandas.

    Args:
    input_value (int or str): A number (or a string representation of a number)
                              to determine the range of operations in the DataFrame.

    Returns:
    str: A string representation of the transformed DataFrame.

    Raises:
    ValueError: If input_value is a string that cannot be converted to an integer.
    """
    import pandas as pd
    import numpy as np

    # Try to parse the input as an integer if it's a string
    if isinstance(input_value, str):
        try:
            input_value = int(input_value)
        except ValueError:
            raise ValueError("Input string could not be converted to an integer")

    # Check if the input is a positive integer
    if not isinstance(input_value, int) or input_value < 1:
        return "Input must be a positive integer"

    # Create a DataFrame with 10 columns of random numbers
    df = pd.DataFrame(np.random.rand(10, 10), columns=[f'Col{i}' for i in range(1, 11)])

    # Calculate the cumulative sum
    df_cumsum = df.cumsum()

    # Select up to the row index specified by the input value
    selected_df = df_cumsum.iloc[:input_value]

    # Return the DataFrame as a string
    return selected_df.head().to_string()

def fibonacci(input_value):
    """
    Calculates the sum of the squares of the Fibonacci sequence up to the n-th term.

    Args:
    input_value (int or str): The number of terms in the Fibonacci sequence to consider
                              (as an integer or a string that can be parsed as an integer).

    Returns:
    int: The sum of the squares of the Fibonacci sequence up to the n-th term.

    Raises:
    ValueError: If input_value is not a positive integer or cannot be parsed as one.
    """

    from functools import lru_cache

    # Try to parse the input as an integer if it's a string
    if isinstance(input_value, str):
        try:
            input_value = int(input_value)
        except ValueError:
            raise ValueError("Input string could not be converted to an integer")

    # Check if the input is a positive integer
    if not isinstance(input_value, int) or input_value < 1:
        raise ValueError("Input must be a positive integer")

    @lru_cache(maxsize=None)  # Cache for Fibonacci function
    def fibonacci(num):
        if num in [1, 2]:
            return 1
        return fibonacci(num - 1) + fibonacci(num - 2)

    if input_value < 35:
        return fibonacci(input_value)

    else:
        logging.warning("Input value is too large to calculate the Fibonacci sequence. Returning input value.")
        return input_value
