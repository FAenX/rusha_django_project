import random


def generate_application_port():

    """Generate a random port for the application.

    Returns:

        int: A random port.

    """

    return random.randint(49152, 65535)