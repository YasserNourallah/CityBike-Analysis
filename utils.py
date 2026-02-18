import os

def validate_positive(value, field_name):
    """Ensures that numerical values like duration and distance are not negative."""
    if value < 0:
        raise ValueError(f"Error: {field_name} cannot be negative ({value}).")
    return value

def ensure_dir(directory):
    """Creates a directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def format_currency(amount):
    """Formats a number as currency string."""
    return f"${amount:,.2f}"