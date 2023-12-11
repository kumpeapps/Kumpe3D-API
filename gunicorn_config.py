import multiprocessing

workers = multiprocessing.cpu_count() * 3 + 1
bind = 'unix:kumpe3dapi.sock'
umask = 0o007
reload = True

#logging
accesslog = '-'
errorlog = '-'
