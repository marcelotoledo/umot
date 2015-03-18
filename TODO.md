* Create service layer
  
  Right now we're connecting directly to the database. We should avoid
  this by creating a micro services layer and this layer will access
  the database. Probably using http://flask.pocoo.org and
  http://www.sqlalchemy.org.
  
  At this moment we need only two interfaces:
  
  1. Persist a link / list of links into the database
  2. Check if a link is already in the database
  
* Create a better solution for existing links

  Right now every time we see a link, we need to check the database if
  it's already in there or it's a new link. This is extremely
  inefficient, find out a new solution for this.
