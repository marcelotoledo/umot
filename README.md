# umot

If you send a URL to umot it will go thru all pages, find all the
links (internal and external) and will identify if there is any broken
links. 

Even if it's a really big website? Yup!


Description
------
umot has 2 major parts:

*umot.py*

This is the worker, what it basically do:
  
* Read the message queue
* Open the url and read it's content
* Update current URL status
* if it exists
  * Identify all URLs (internal and external)
  * Insert all of them into the message queue to be processed
*  * Persist them into the database
    
*umotws.py*
  
This is the middleware with all the webservices responsible for
persisting information into the database.

Besides these two major parts we use RabbitMQ
(http://www.rabbitmq.com) as the message queue and this allow us to
scale horizontally to an impressive number of servers. We are also
using Flask (http://flask.pocoo.org) in the middleware together with
SQLAlchemy (http://www.sqlalchemy.org) and as a database PostgreSQL.
    

Requirements
------

pip install -r requirements.txt (missing update)

Usage
------

Before anything you need to set up the database:
        
* Install PostgreSQL and make sure it's up & running
* createdb umot
* psql
  * CREATE USER umot WITH PASSWORD 'RabrXfC9ggBhyFWBsWAWoH3';
* Go to the main dir of umot
* python
  * import model, db
  * db.create_all() - There is a db.drop_all() as well.*
* python umotws.py - Run the middleware
* ./umot.py - Run the worker

RabbitMQ
------

To send a new message:
    
    > rabbitmqadmin publish exchange=amq.default routing_key=umot_queue payload="message"
    
Pop message from the queue:
    
    > rabbitmqadmin purge queue name=umot_queue
