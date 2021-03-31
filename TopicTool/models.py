
from TopicTool import db

class TopicToolDB(db.Model):
    ''' define table columns '''
    id=db.Column(db.Integer,primary_key=True)
    subject = db.Column(db.Text,unique=False,nullable=True)
    case_description = db.Column(db.Text,unique=False, nullable=True)

    def __init__(self, data):
        self.data = data

    def fillTable(self):
        for i in range(self.data.shape[0]):
            # fill row by row
            db.session.add()

    #def buildTable(self):
    #    self.removeBadCols()
    #    col_names=self.data.columns
    #    col_types=self.data.dtypes
    #    db_col_types={"float":db.Float, 
    #                  "int":db.Int, 
    #                  "datetime":db.DateTime,
    #                  "object":db.Text}
    #    for i,col in enumerate(col_names):
    #        if "float" in col_types[i]:
    #            db.Column(db_col_types["float"], unique=False, nullable=True)
    #        elif "int" in col_types[i]:
    #            db.Column(db_col_types["int"], unique=False, nullable=True)
    #        elif "datetime" in coltypes[i]:
    #            db.Column(db_col_types["datetime"], unique=False, nullable=True)
    #        elif "object" in coltypes[i]:
    #            db.Column(db_col_types["object"], unique=False, nullable=True)
    #        else:
    #            print("Unknown data type {} for column {} - skipping it.".format(col_types[i], col))
    #            pass
    #
    #    # loop through rows then commit

        
    def removeBadCols(self):
        cols = self.data.columns
        bad_cols = [x for x in cols if "Unnamed" in x]
        self.data.drop(labels = bad_cols)

    username = db.Column(db.String(80), unique=True, nullable=False)

    # look at other arguments - unique, nullable, etc.
    # loop through the columns/types in the input - are there 
    # other types besides String(count) for long free text?

    # look into sqlalchemy to understand these classes for the db