import logging as log
from datetime import datetime, timedelta


def reduct(data, start_time, end_time, period):
    """Redukuje vstupni pouze na urcite obdobi od start_time do end_time a provede vzorkovani o velikosti period"""
    zero_time = datetime.fromtimestamp(0)
    zero_period = timedelta(seconds=0)

    if start_time < zero_time or end_time <= zero_time or start_time >= end_time or period <= zero_period:
        log.warning("Can not reduce list. Input times are invalid.")
        return []

    if (end_time - start_time)/period > len(data):
        log.warning("Can not reduce list. Data set is too small.")
        return []

    bpm_sum = 0
    counter = 0
    result = []
    try:
        for row in data:
            if start_time >= end_time:
                return result
            if row[0] < start_time:
                continue
            if row[0] - start_time >= period and counter is not 0:
                result.append((start_time, bpm_sum / counter))
                bpm_sum = counter = 0
                start_time += period

            if row[1] is not 0:
                bpm_sum += row[1]
                counter += 1

        if counter is not 0:
            result.append((start_time, bpm_sum / counter))

    except TypeError:
        log.warning("Can not reduce list. Incompatible type.")
        return []

    return result
