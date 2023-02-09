"""

Explanation
Example case 1. The sequence is already sorted.

Example case 2. The sequence is not sorted.

"""


def almost_sorted(arr):
    """
    >>> almost_sorted([1, 2, 3])
    'YES'
    >>> almost_sorted([2, 4, 1, 3, 5])
    'NO'
    >>> almost_sorted([1, 2, 5, 3, 4])
    'YES'
    """
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        return 'YES'
    else:
        for i in range(len(arr)):
            if arr[i] != sorted_arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                if arr == sorted_arr:
                    return 'YES'
                else:
                    return 'NO'


if __name__ == "__main__":
    import doctest
    doctest.testmod()