import os
import sys
import pyowm 
import psutil
import platform
from pyowm.owm import OWM
from datetime import datetime

BYTE_TO_MEGABYTE = 0.00000095367432

class Memory:
    def __init__(self, memory, memory_total, memory_free, memory_used, memory_limit):
        self.memory = psutil.virtual_memory() 
        self.memory_total = getattr(memory, 'total') * BYTE_TO_MEGABYTE 
        self.memory_free = getattr(memory, 'free') * BYTE_TO_MEGABYTE 
        self.memory_used = getattr(memory, 'used') 
        self.memory_limit = (memory_used / 100 * 20) * BYTE_TO_MEGABYTE # 20% of the RAM 

class Disk:
    def __init__(self, disk, disk_free, disk_total, disk_used, disk_limit):
        self.disk = psutil.disk_usage('/')
        self.disk_free = getattr(disk, 'free') * BYTE_TO_MEGABYTE
        self.disk_total = getattr(disk, 'total') * BYTE_TO_MEGABYTE
        self.disk_used = getattr(disk, 'used')
        self.disk_limit = (disk_used / 100 * 20) * BYTE_TO_MEGABYTE # 20% of the disk

# weather
city = 'Tallinn'
owm = OWM('API KEY')
manager = owm.weather_manager()
observation = manager.weather_at_place(city)
weather = observation.weather

# information about both
def memory_info():
    print('RAM:')
    print('Your total memory: ', round(memory_total, 2), 'MB')
    print('Memory available: ', round(memory_free, 2), 'MB')

def disk_info():
    print('\nDisk usage:')
    print('Your total disk memory: ', round(disk_free, 2), 'MB')
    print('Disk memory available: ', round(disk_total, 2), 'MB')

# this block of code is required because Microsoft's cmd uses "cls" instead of "clear"
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

memory_info()
disk_info()

if memory_used > memory_limit:
    print('WARNING: You are using more than 20% of your RAM')
elif disk_used > disk_limit:
    print('WARNING: You are using more than 20% of your disk space')

input()
    
# entering history of the progarm in the "history.txt"
with open('history.txt', mode='a')as history:
    current_time = str(datetime.now()) 

    history.write(current_time)
    history.write(str(weather))
    history.write('\nRAM:\n')
    history.write(str(round(memory_total, 2)))
    history.write('\n')
    history.write(str(round(memory_free, 2)))
    history.write('\n')

    history.write('\ndisk:\n')
    history.write(str(round(disk_free, 2)))
    history.write('\n')
    history.write(str(round(disk_total, 2)))
    history.write('\n\n')

    history.close()
