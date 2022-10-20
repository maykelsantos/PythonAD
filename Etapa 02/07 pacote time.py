import time

print('Comecei a gora [...]')
time.sleep(1)
print('1 [...]')
time.sleep(1)
print('2 [...]')
time.sleep(1)
print('3 [...]')
time.sleep(1)
print('Terminei!')

#----------#

agora = time.localtime()
print(agora)
print(type(agora))

#----------#

print(time.strftime('%d/%m/%y, %H:%M:%S', agora))