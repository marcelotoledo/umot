import sys
import ummq

def callback():
    pass

mq = ummq.UMMQueue('localhost', 'umot_queue', callback)

mq.open()
message = ' '.join(sys.argv[1:]) or "Hello World!"
mq.write(message)
