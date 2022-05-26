import psutil
from hurry.filesize import size

#memory
memory = psutil.virtual_memory()
memory_total = size(getattr(memory, 'total'))  
memory_in_use = size(getattr(memory, 'free'))

print('RAM:\n')
print('your total memory: ', memory_total)
print('memory available: ', memory_in_use)

#disk
disk = psutil.disk_usage('/')
disk_free = size(getattr(disk, 'total'))
disk_total = size(getattr(disk, 'free'))

print('Disk usage:\n')
print('your total disk memory: ', disk_free)
print('disk memory available: ', disk_total)
