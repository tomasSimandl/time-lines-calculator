
def reduct(data, start_time, end_time, period):
    """Redukuje vstupni pouze na urcite obdobi od start_time do end_time a provede vzorkovani o velikosti period"""
    bpm_sum = 0
    counter = 0
    result = []

    for row in data:
        if start_time > end_time:
            return result
        if row[0] < start_time:
            continue
        if row[0] - start_time >= period and counter is not 0:
            item = (start_time, bpm_sum / counter)
            result.append(item)
            bpm_sum = counter = 0
            start_time += period

        if row[1] is not 0:
            bpm_sum += row[1]
            counter += 1

    return result
