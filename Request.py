class Rec():
    def __init__(self, con):
            self.con = con
            self.cursorObj = con.cursor()