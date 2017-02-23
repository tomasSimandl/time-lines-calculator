from datetime import datetime
import csv

time_definition = {'s': 'seconds', 'ms': 'milliseconds', 'us': 'microseconds'}


def time_convert(time_value, time_format):
    """Převede hodnotu time_value do datetime formátu. time_format udává formát time_value."""
    if time_format is time_definition['s']:
        return datetime.fromtimestamp(int(time_value))

    if time_format is time_definition['ms']:
        return datetime.fromtimestamp(int(int(time_value)/1000))

    if time_format is time_definition['us']:
        return datetime.fromtimestamp(int(int(time_value)/1000000))

    return datetime.strptime(time_value, time_format)


def global_reader(reader, time_index, hr_index, time_format):
    """Nacita po radcich z reader a prevadi jednotlive radky na seznam obsahujici cas a tepovou frekvenci"""
    data_list = []
    for row in reader:
        time = time_convert(row[time_index], time_format)

        if row[hr_index]:
            hr = int(row[hr_index])
        else:
            hr = 0

        item = (time, hr)
        data_list.append(item)

    return data_list


def csv_reader(file_name, delimiter, time_index, hr_index, time_format, skip_header):
    """Pouziva funkci global_reader a jako vstup je pouzit nacteny csv soubor"""
    with open(file_name, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=delimiter)
        if skip_header:
            next(reader)
        return global_reader(reader, time_index, hr_index, time_format)


def strap_reader(file_name):
    """Pouziva funkci csv_reader, ale ma definovan format dat"""
    return csv_reader(file_name, ',', 0, 2, time_definition['ms'], False)


def basis_peak_reader(file_name):
    """Pouziva funkci csv_reader, ale ma definovan format dat pro basis peak hodinky"""
    return csv_reader(file_name, ',', 1, 4, '%Y-%m-%d %H:%M:%S', True)
