import os
import psutil
import platform

BYTE_TO_MEGABYTE = 0.00000095367432

#memory
memory = psutil.virtual_memory()
memory_total = getattr(memory, 'total') * BYTE_TO_MEGABYTE
memory_free = getattr(memory, 'free') * BYTE_TO_MEGABYTE
memory_used = getattr(memory, 'used') 
memory_limit = (memory_used / 100 * 20) * BYTE_TO_MEGABYTE

#disk
disk = psutil.disk_usage('/')
disk_free = getattr(disk, 'total') * BYTE_TO_MEGABYTE
disk_total = getattr(disk, 'free') * BYTE_TO_MEGABYTE
disk_used = getattr(disk, 'used') 
disk_limit = (disk_used / 100 * 20) * BYTE_TO_MEGABYTE

# this block of code is required because Microsoft's cmd doesn't use "clear"
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

print('RAM:')
print('Your total memory: ', round(memory_total, 2), 'MB')
print('Memory available: ', round(memory_free, 2), 'MB')

print('\nDisk usage:')
print('Your total disk memory: ', round(disk_free, 2), 'MB')
print('Disk memory available: ', round(disk_total, 2), 'MB')

if memory_used > memory_limit:
    print('WARNING: You are using more than 20% of your RAM')
elif disk_used > disk_limit:
    print('WARNING: You are using more than 20% of your disk space')
