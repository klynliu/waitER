from collections import namedtuple
from operator import attrgetter
import bisect
import random
import sys
'''                                                                                                                                                            
Interval scheduling for patients weighted on ESI                                                                                                               
'''

Patient = namedtuple('Patient', 'ID start_time end_time duration ESI')

# stores file in dictionary of named tuples                                                                                                                    
def make_list(file="/Users/Tongyu/hackathon/PennApps/data/ESI.data.csv"):
    list = []
    with open(file) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    content.pop(0)
    for line in content:
        l = line.split(',')
        list.append(Patient(l[0][1:-1], l[2][1:-1], l[3][1:-1], random.randint(1,101), l[4]))
    patients = sorted(list, key=attrgetter('ESI'))
    print(patients, flush=True)

def schedule(patient, list):
    l = patient.split(',')
    list.append(Patient(l[0][1:-1], l[2][1:-1], l[3][1:-1], random.randint(1,101), l[4]))
    patients = sorted(list, key=attrgetter('ESI'))
    print(patients, flush=True)

if __name__ == '__main__':
#    filename = "/Users/Tongyu/hackathon/PennApps/data/ESI.data.csv"                                                                                           
    make_list()
