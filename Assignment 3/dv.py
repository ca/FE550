import numpy as np
import matplotlib.pyplot as plt
import csv

# 1. reading the csv
status_records = {'1': {}, '-11': {}}

with open('RescueTimeData.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    # 2. iterate through csv
    for row in reader:
        if row[0] == 'Date': continue # first line
        hour = row[0][:-5]
        status = row[1]

        # if hour not present, add empty 'slot' in each status bin
        if hour not in status_records[status].keys():
            status_records['1'][hour] = 0
            status_records['-11'][hour] = 0
            status_records[status][hour] = 1 # add the status we just read
        else:
            status_records[status][hour] += 1 # update status-hour bin

status1   = status_records['1'].values()
status2 = status_records['-11'].values()

print status1, status2

N = len(status1)
ind = np.arange(N)
width = 0.35

p1 = plt.bar(ind, status1, width, color='g')
p2 = plt.bar(ind, status2, width, color='r', bottom=status1)

plt.ylabel('# of exit status')
plt.title('Exit status in comparison with time')
plt.yticks(np.arange(0,11,10))
plt.legend((p1[0], p2[0]), ('1', '-11'))
plt.show()