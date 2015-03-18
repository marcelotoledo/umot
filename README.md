# umot

umot is a software that reads a url from the command line and returns
the following info:

     * Amount of internal URLs
     * List of internal broken links
     * Amount of external links
     * List of external broken links

Requirements
------
     pip install -r requirements.txt

Usage
------

     python umot.py http://foo.bar/

RabbitMQ
------

    To send a new message:
    
    rabbitmqadmin publish exchange=amq.default routing_key=queue_name payload="message"
    
    Pop message from the queue:
    
    rabbitmqadmin purge queue name=queue_name
