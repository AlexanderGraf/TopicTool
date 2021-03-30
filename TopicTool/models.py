
from TopicTool import db

class TopicToolDB(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    

    # look at other arguments - unique, nullable, etc.
    # loop through the columns/types in the input - are there 
    # other types besides String(count) for long free text?

    # look into sqlalchemy to understand these classes for the db