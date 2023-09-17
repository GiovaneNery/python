"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# "TODO: define the 'EXPECTED_BAKE_TIME' constant."
EXPECTED_BAKE_TIME = 40 # Expected baking time for the lasagna (in minutes)

# "TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below."
def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining bake time.

    :param elapsed_bake_time: int - baking time already elapsed (in minutes).
    :return: int - remaining bake time (in minutes).

    This function calculates the remaining bake time for the lasagna by subtracting
    the elapsed bake time from the expected bake time.

    Example:
    >>> bake_time_remaining(20)
    20  # If 20 minutes have already passed, 20 minutes of baking time remain.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

PREPARATION_TIME = 2 # Preparation time for each layer (in minutes)

# "TODO: Define the 'preparation_time_in_minutes()' function below."
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the total preparation time.

    :param number_of_layers: int - number of lasagna layers.
    :return: int - total preparation time (in minutes).

    This function calculates the total preparation time for the lasagna based on the
    number of layers and the constant PREPARATION_TIME.

    Example:
    >>> preparation_time_in_minutes(3)
    6  # For 3 layers, the total preparation time is 3 layers x 2 minutes/layer = 6 minutes.
    """
    return number_of_layers * PREPARATION_TIME

# "TODO: define the 'elapsed_time_in_minutes()' function below."
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time in minutes.

    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes).

    Function that calculates the total elapsed time in minutes by summing the
    preparation time (based on 'PREPARATION_TIME') and the time the lasagna
    has already spent baking in the oven.

    Example:
    >>> elapsed_time_in_minutes(3, 20)
    26  # 3 layers x 2 minutes each for preparation + 20 minutes already baked.
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)
    total_elapsed_time = preparation_time + elapsed_bake_time
    return total_elapsed_time
