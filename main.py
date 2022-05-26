import psutil
from hurry.filesize import size

memory = psutil.virtual_memory()

memory_total = size(getattr(memory, 'total'))  
memory_in_use = size(getattr(memory, 'free'))

print('RAM:\n')
print('your total memory: ', memory_total)
print('memory available: ', memory_in_use)
