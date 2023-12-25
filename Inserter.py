class DataInserter():
    def __init__(self, con):
        self.con = con
        self.cursorObj = self.con.cursor()
    
    def patient(self, name, passportDetails, telephone, city, user_address, user_gender,
             user_datetime, user_age, user_height, user_weight,
             user_briefDescriptionComplaintsDate, user_allergicReactions,
             user_hyperallergicReactionstonicDisease, user_takeHyperallergicMedications,
             user_cardiacIschemia, user_cerebrovascularDisease, user_chronicDisease,
             user_tuberculosis, user_diabetes, user_takeMedications,
             user_stomachDiseases, user_chronicKidneyDisease, user_malignantNeoplasm,
             user_whichMalignantNeoplasm, user_elevatedСholesterol,
             user_drugsElevatedСholesterol, user_myocardium,
             user_stroke, user_myocardialInfarction, user_Relatives,
             user_chestDiscomfort, user_ifChestDiscomfort, user_termWeakness,
             user_numbness, user_visionLoss, user_cough, user_wheezing,
             user_hemoptysis, user_upperAbdomen, user_poop, user_lostWeight,
             user_holes, user_bleeding, user_smoke, user_howManySmoke, user_walking,
             user_diet, user_addSomeSalt, user_narcotic, user_quantityAlcoholic,
             user_youUseAlcoholic, user_totalPoints, user_countPoints,
             user_otherComplaints):
        
        self.cursorObj.execute("INSERT INTO patient (name, passportDetails, telephone, city, user_address, user_gender, user_datetime, user_age, user_height,user_weight,\
                            user_briefDescriptionComplaintsDate,user_allergicReactions,\
                            user_hyperallergicReactionstonicDisease,user_takeHyperallergicMedications,\
                            user_cardiacIschemia,user_cerebrovascularDisease,user_chronicDisease,user_tuberculosis,\
                            user_diabetes,user_takeMedications,user_stomachDiseases,\
                            user_chronicKidneyDisease,user_malignantNeoplasm,user_whichMalignantNeoplasm,\
                            user_elevatedСholesterol,user_drugsElevatedСholesterol,user_myocardium,\
                            user_stroke,user_myocardialInfarction,user_Relatives,user_chestDiscomfort,\
                            user_ifChestDiscomfort,user_termWeakness,user_numbness,user_visionLoss,\
                            user_cough,user_wheezing,user_hemoptysis,user_upperAbdomen,user_poop,\
                            user_lostWeight,user_holes,user_bleeding,user_smoke,user_howManySmoke,\
                            user_walking,user_diet,user_addSomeSalt,user_narcotic,user_quantityAlcoholic,\
                            user_youUseAlcoholic,user_totalPoints,\
                            user_countPoints,\
                            user_otherComplaints) VALUES(?,?,?,?,?,?,?,?,?,?,\
                                                        ?,?,?,?,?,?,?,?,?,?,\
                                                        ?,?,?,?,?,?,?,?,?,?,\
                                                        ?,?,?,?,?,?,?,?,?,?,\
                                                        ?,?,?,?,?,?,?,?,?,?,\
                                                        ?,?,?,?)", 
                                                        (name, passportDetails, telephone, 
                                                        city, user_address, user_gender, 
                                                        user_datetime, user_age,user_height,
                                                        user_weight,user_briefDescriptionComplaintsDate,
                                                        user_allergicReactions,user_hyperallergicReactionstonicDisease,
                                                        user_takeHyperallergicMedications,user_cardiacIschemia,
                                                        user_cerebrovascularDisease,user_chronicDisease,
                                                        user_tuberculosis,user_diabetes,user_takeMedications,
                                                        user_stomachDiseases,user_chronicKidneyDisease,
                                                        user_malignantNeoplasm,user_whichMalignantNeoplasm,
                                                        user_elevatedСholesterol,user_drugsElevatedСholesterol,
                                                        user_myocardium,user_stroke,user_myocardialInfarction,
                                                        user_Relatives,user_chestDiscomfort,user_ifChestDiscomfort,
                                                        user_termWeakness,user_numbness,user_visionLoss,user_cough,
                                                        user_wheezing,user_hemoptysis,user_upperAbdomen,user_poop,
                                                        user_lostWeight,user_holes,user_bleeding,user_smoke,
                                                        user_howManySmoke,user_walking,user_diet,user_addSomeSalt,
                                                        user_narcotic,user_quantityAlcoholic,user_youUseAlcoholic,
                                                        user_totalPoints,user_countPoints,user_otherComplaints))

    def insert_data(self, name, passportDetails, telephone, city, user_address, user_gender, user_datetime,
                user_age,user_height,user_weight,user_briefDescriptionComplaintsDate,user_allergicReactions,
                user_hyperallergicReactionstonicDisease,user_takeHyperallergicMedications,user_cardiacIschemia,
                user_cerebrovascularDisease,user_chronicDisease,user_tuberculosis,user_diabetes,user_takeMedications,
                user_stomachDiseases,user_chronicKidneyDisease,user_malignantNeoplasm,user_whichMalignantNeoplasm,
                user_elevatedСholesterol,user_drugsElevatedСholesterol,user_myocardium,user_stroke,
                user_myocardialInfarction,user_Relatives,user_chestDiscomfort,user_ifChestDiscomfort,user_termWeakness,user_numbness,
                user_visionLoss,user_cough,user_wheezing,user_hemoptysis,user_upperAbdomen,user_poop,user_lostWeight,
                user_holes,user_bleeding,user_smoke,user_howManySmoke,user_walking,user_diet,user_addSomeSalt,user_narcotic,
                user_quantityAlcoholic,user_youUseAlcoholic,user_totalPoints,user_countPoints,user_otherComplaints):
        
        self.patient(f"{name}",f"{passportDetails}",f"{telephone}",f"{city}",f"{user_address}",f"{user_gender}",
                    f"{user_datetime}",f"{user_age}",f"{user_height}",f"{user_weight}",
                    f"{user_briefDescriptionComplaintsDate}",f"{user_allergicReactions}",
                    f"{user_hyperallergicReactionstonicDisease}",f"{user_takeHyperallergicMedications}",
                    f"{user_cardiacIschemia}",f"{user_cerebrovascularDisease}",f"{user_chronicDisease}",
                    f"{user_tuberculosis}",f"{user_diabetes}",f"{user_takeMedications}",
                    f"{user_stomachDiseases}",f"{user_chronicKidneyDisease}",f"{user_malignantNeoplasm}",
                    f"{user_whichMalignantNeoplasm}",f"{user_elevatedСholesterol}",
                    f"{user_drugsElevatedСholesterol}",f"{user_myocardium}",
                    f"{user_stroke}",f"{user_myocardialInfarction}",f"{user_Relatives}",
                    f"{user_chestDiscomfort}",f"{user_ifChestDiscomfort}",f"{user_termWeakness}",
                    f"{user_numbness}",f"{user_visionLoss}",f"{user_cough}",f"{user_wheezing}",
                    f"{user_hemoptysis}",f"{user_upperAbdomen}",f"{user_poop}",f"{user_lostWeight}",
                    f"{user_holes}",f"{user_bleeding}",f"{user_smoke}",f"{user_howManySmoke}",f"{user_walking}",
                    f"{user_diet}",f"{user_addSomeSalt}",f"{user_narcotic}",f"{user_quantityAlcoholic}",
                    f"{user_youUseAlcoholic}",f"{user_totalPoints}",f"{user_countPoints}",
                    f"{user_otherComplaints}")

        self.con.commit()

    