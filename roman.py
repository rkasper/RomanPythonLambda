def convert(roman):
    """
    Converts Roman strings to plain old integers

    Input: roman, a Roman numeric value, for example I, V, X, XXX, MMXX
    Output: the regular integer equivalent of the Roman input
    """

    if roman == "I":
        return 1
    elif roman == "V":
        return 5
    elif roman == "X":
        return 10
    elif roman == "L":
        return 50
    elif  roman == "C":
        return 100
    else:
        return 500
