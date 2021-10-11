import sys,time

class Logger(object):
    def __init__(self, filename='train.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

tm = time.localtime()
sys.stdout = Logger('Model_{0}_{1}_{2}_{3}.log'.format(tm.tm_mon,tm.tm_mday,tm.tm_hour,tm.tm_min), sys.stdout)
print("测试")
