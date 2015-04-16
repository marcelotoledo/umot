import ummq

version = "0.1"

def callback(ch, method, properties, body):
    print(" [*] Recebi %s" % body)
    mq.ack(method)

if __name__ == '__main__':
    print("umot ver %s - Copyright 2014 (C) Marcelo Toledo\n" % version)

    mq = ummq.UMMQueue('localhost', 'umot_queue', callback)

    mq.open()
    print(' [*] Waiting for the next item in queue')
    mq.consume()
