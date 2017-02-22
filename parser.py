from datetime import datetime
from datetime import timedelta
import calculations.data_reduction as reductor
import calculations.calculations as calculation
import data_reading.reading as reader

startTime = 1479115320
fileName = 'HRData14112016105304.csv'

#startTime = 1479117600
#fileName = 'HRData14112016113304.csv'

#startTime = 1479120120
#fileName = 'HRData14112016121521.csv'

#startTime = 1480926000
#fileName = 'HRData05122016095206.csv'

#startTime = 1480928820
#fileName = 'HRData05122016103718.csv'

#startTime = 1481016060
#ileName = 'HRData06122016105301.csv'

expected_list = reader.strap_reader(fileName)
measured_list = reader.basis_peak_reader('minute-metrics-2016-11.csv')

start_time = datetime.fromtimestamp(startTime)
end_time = datetime.fromtimestamp(startTime+1740)
period_time = timedelta(seconds=60)

expected_list_reduced = reductor.reduct(expected_list, start_time, end_time, period_time)
measured_list_reduced = reductor.reduct(measured_list, start_time, end_time, period_time)

for i in range(len(expected_list_reduced)):
    print(expected_list_reduced[i][1], end=' - ')
    print(measured_list_reduced[i][1])

print()

print('DW  : ' + str(calculation.durbin_watson_test(measured_list_reduced, expected_list_reduced)))
print('AVG : ' + str(calculation.average_error(measured_list_reduced, expected_list_reduced)))
print('AAVG: ' + str(calculation.abs_average_error(measured_list_reduced, expected_list_reduced)))
print('ROZP: ' + str(calculation.dispersion_calculation(measured_list_reduced, expected_list_reduced)))
print('SMER: ' + str(calculation.standard_deviation(measured_list_reduced, expected_list_reduced)))

