from decimal import ROUND_HALF_UP, Decimal


def isDecimal(num: Decimal) -> bool:
    """Check if the input is a Decimal."""
    return isinstance(num, Decimal)


def isDecimalThrow(num: Decimal):
    """Check if the input is a Decimal, if not, raise ValueError."""
    if not isinstance(num, Decimal):
        raise ValueError("num is not a Decimal")


def decimals_eq_precision(a: Decimal, b: Decimal, precision: int = 10) -> bool:
    """
    Compare two Decimal numbers by rounding them to a specified precision
    and check if the rounded values are equal.

    Args:
    - a: First Decimal number to compare.
    - b: Second Decimal number to compare.
    - precision: Number of decimal places to consider in the comparison. Default is 10.

    Returns:
    - True if the rounded values are equal, False otherwise.
    """
    rounded_a = a.quantize(Decimal("1e-{0}".format(precision)), rounding=ROUND_HALF_UP)
    rounded_b = b.quantize(Decimal("1e-{0}".format(precision)), rounding=ROUND_HALF_UP)
    return rounded_a == rounded_b


def find_first_difference(a: Decimal, b: Decimal) -> int:
    """
    Find the index of the first differing digit between two Decimal numbers.

    Args:
    - a: First Decimal number.
    - b: Second Decimal number.

    Returns:
    - Index of the first differing digit, starting from the right (least significant digit).
      Returns -1 if the numbers are identical.
    """
    str_a = str(a)
    str_b = str(b)

    # Find the length of the shorter string
    length = min(len(str_a), len(str_b))

    # Compare digits starting from the right (least significant digit)
    for i in range(length):
        if str_a[-(i + 1)] != str_b[-(i + 1)]:
            return i

    # If no difference is found in the overlapping part,
    # check if the longer string has additional non-zero digits
    for i in range(length, max(len(str_a), len(str_b))):
        if len(str_a) > len(str_b):
            if str_a[-(i + 1)] != "0":
                return i
        else:
            if str_b[-(i + 1)] != "0":
                return i

    # If both strings are identical
    return -1
