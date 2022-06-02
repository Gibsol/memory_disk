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

    def memory_info(self):
        print('RAM:')
        print('Your total memory: ', round(self.memory_total, 2), 'MB')
        print('Memory available: ', round(self.memory_free, 2), 'MB')

        if self.memory_used > self.memory_limit:
            print('WARNING: You are using more than 20% of your RAM')

class Disk:
    def __init__(self, disk, disk_free, disk_total, disk_used, disk_limit):
        self.disk = psutil.disk_usage('/')
        self.disk_free = getattr(disk, 'free') * BYTE_TO_MEGABYTE
        self.disk_total = getattr(disk, 'total') * BYTE_TO_MEGABYTE
        self.disk_used = getattr(disk, 'used')
        self.disk_limit = (disk_used / 100 * 20) * BYTE_TO_MEGABYTE # 20% of the disk
    
    def disk_info(self):
        print('\nDisk usage:')
        print('Your total disk memory: ', round(self.disk_free, 2), 'MB')
        print('Disk memory available: ', round(self.disk_total, 2), 'MB')

        if self.disk_used > self.disk_limit:
            print('WARNING: You are using more than 20% of your disk space')
        
# weather
city = 'Tallinn'
owm = OWM('API KEY')
manager = owm.weather_manager()
observation = manager.weather_at_place(city)
weather = observation.weather

# this block of code is required because Microsoft's cmd uses "cls" instead of "clear"
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

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
