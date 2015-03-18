# ummq.py --- message queue

# Copyright  (C)  2015  Marcelo Toledo <marcelo@marcelotoledo.com>

# Version: 1.0
# Keywords: 
# Author: Marcelo Toledo <marcelo@marcelotoledo.com>
# Maintainer: Marcelo Toledo <marcelo@marcelotoledo.com>
# URL: http://

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

# Commentary: 

# Sample usage would be:

# def callback():
#     print('Callback!')

# mq = ummq.MQueue('localhost', 'task_queue', callback)

# mq.open()
# mq.write('hello world!')
# mq.consume()
# mq.close()

# Code:

import pika

class UMMQueue:
    def __init__(self, host, queue, callback):
        self.host       = host
        self.connection = None
        self.ch         = None
        self.queue      = queue
        self.callback   = callback

    def open(self): 
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel()

    def close(self):
        self.connection.close()

    def write(self, message):
        self.ch.basic_publish(exchange='',
                              routing_key=self.queue,
                              body=message,
                              properties=pika.BasicProperties(delivery_mode = 2, # make message persistent
                                ))
    def consume(self):
        self.ch.basic_qos(prefetch_count=1)
        self.ch.basic_consume(self.callback, queue=self.queue)
        self.ch.start_consuming()

    # ackknowledge message
    def ack(self, method):
        self.ch.basic_ack(delivery_tag = method.delivery_tag)

    def channel(self):
        self.ch = self.connection.channel()
        self.ch.queue_declare(queue=self.queue, durable=True)
