import db
from sqlalchemy import Sequence, ForeignKey, func
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, backref

class Website(db.Base):
    __tablename__ = 'website'

    id      = Column(Integer, Sequence('website_id_seq'), primary_key=True)
    website = Column(String, nullable=False)

    links   = relationship("Link", order_by="Link.id", backref="website")

class Link(db.Base):
    __tablename__ = 'link'

    id         = Column(Integer, Sequence('link_id_seq'), primary_key=True)
    website_id = Column(Integer, ForeignKey('website.id'), nullable=False)
    link       = Column(String,  nullable=False)
    internal   = Column(Boolean, server_default='True')
    processed  = Column(Boolean, server_default='False')
    created_at = Column(String)
    updated_at = Column(String)
