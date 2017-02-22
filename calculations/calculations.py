from math import pow
from math import sqrt


def residues_calculation(measured, expected):
    """Vyrati seznam rezidui namerenych dat. Neshoduji-li se delky vstupnich seznamu, vraci prazdny seznam."""
    result = []
    if len(measured) is not len(expected):
        return result

    for i in range(len(measured)):
        result.append(measured[i][1] - expected[i][1])

    return result


def durbin_watson_test(measured, expected):
    """Spocita hodnotu Durbin-Watson testu autokorelovanosti namerene casove rady. Pri neuspechu vraci None."""
    residues = residues_calculation(measured, expected)
    if len(residues) is 0:
        return None

    numerator = 0
    denominator = 0

    for i in range(1, len(residues)):
        numerator += pow(residues[i] - residues[i - 1], 2)

    for i in range(len(residues)):
        denominator += pow(residues[i], 2)

    return numerator/denominator


def average_error(measured, expected):
    """Spocita prumernou chybu namerenych dat. Pri neuspechu vraci None."""
    residues = residues_calculation(measured, expected)
    if len(residues) is 0:
        return None

    return sum(residues)/len(residues)


def abs_average_error(measured, expected):
    """Spocita prumernou absolutni chybu namerenych dat. Pri neuspechu vraci None."""
    residues = residues_calculation(measured, expected)
    if len(residues) is 0:
        return None

    residues_sum = 0
    for err in residues:
        residues_sum += abs(err)

    return residues_sum/len(residues)


def dispersion_calculation(measured, expected):
    """Spocita rozptyl namerenych dat oproti ocekavanym. Pri neuspechu vraci None."""
    residues = residues_calculation(measured, expected)
    if len(residues) is 0:
        return None

    square_sum = 0
    for err in residues:
        square_sum += pow(err, 2)

    return square_sum/len(residues)


def standard_deviation(measured, expected):
    """Spocita smerodatnou odchylku namerenych dat oproti ocekavanym. Pri neuspechu vraci None."""
    dispersion = dispersion_calculation(measured, expected)
    if dispersion is None:
        return None

    return sqrt(dispersion)
