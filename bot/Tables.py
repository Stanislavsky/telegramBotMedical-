class MyTables():
    def __init__(self, con):
        self.con = con
        self.cursor = con.cursor()

    def sql_tables(self):
        cursorObj = self.con.cursor()
        cursorObj.execute("""
            CREATE TABLE IF NOT EXISTS patient (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                passportDetails TEXT,
                telephone INTEGER,
                city TEXT,
                user_address TEXT,
                user_gender TEXT,
                user_datetime TEXT,
                user_age TEXT,
                user_height TEXT,
                user_weight TEXT,
                user_briefDescriptionComplaintsDate TEXT,
                user_allergicReactions TEXT,
                user_hyperallergicReactionstonicDisease TEXT,
                user_takeHyperallergicMedications TEXT,
                user_cardiacIschemia TEXT,
                user_cerebrovascularDisease TEXT,
                user_chronicDisease TEXT,
                user_tuberculosis TEXT,
                user_diabetes TEXT,                       
                user_takeMedications TEXT,
                user_stomachDiseases TEXT,
                user_chronicKidneyDisease TEXT,
                user_malignantNeoplasm TEXT,
                user_whichMalignantNeoplasm TEXT,
                user_elevatedСholesterol TEXT,
                user_drugsElevatedСholesterol TEXT,
                user_myocardium TEXT,
                user_stroke TEXT,
                user_myocardialInfarction TEXT,
                user_Relatives TEXT,
                user_chestDiscomfort TEXT,
                user_ifChestDiscomfort TEXT,                       
                user_termWeakness TEXT,
                user_numbness TEXT,
                user_visionLoss TEXT,
                user_cough TEXT,
                user_wheezing TEXT,
                user_hemoptysis TEXT,
                user_upperAbdomen TEXT,
                user_poop TEXT,
                user_lostWeight TEXT,
                user_holes TEXT,
                user_bleeding TEXT,
                user_smoke TEXT,
                user_howManySmoke TEXT,                       
                user_walking TEXT,
                user_diet TEXT,
                user_addSomeSalt TEXT,
                user_narcotic TEXT,
                user_quantityAlcoholic TEXT,                       
                user_youUseAlcoholic TEXT,
                user_totalPoints TEXT,
                user_countPoints TEXT,
                user_otherComplaints TEXT
            )""")
        self.con.commit()