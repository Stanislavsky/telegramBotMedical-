from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    user_name = State()
    ###################
    user_passport = State()
    user_city = State()
    ###########################
    user_address = State()
    user_telephone = State()
    user_gender = State()
    user_age = State()
    user_height= State()
    user_weight= State()
    user_briefDescriptionComplaintsDate= State()
    user_allergicReactions= State()
# # 8)Хронические заболевания
    user_hyperallergicReactionstonicDisease= State() # да нет
    user_takeHyperallergicMedications = State() # какие
    user_cardiacIschemia= State()
    user_cerebrovascularDisease= State()
    user_chronicDisease = State()
    user_tuberculosis= State()
    user_diabetes= State() # да нет
    user_takeMedications = State()
    user_stomachDiseases= State()
    user_chronicKidneyDisease= State()
    user_malignantNeoplasm = State()# да нет
    user_whichMalignantNeoplasm = State()
    user_elevatedСholesterol = State()# да нет
    user_drugsElevatedСholesterol = State() 
    user_myocardium= State()
    user_stroke= State()
    user_myocardialInfarction= State()
    
    user_Relatives = State()
    user_chestDiscomfort= State() # да нет
    user_ifChestDiscomfort= State() #какие?
    user_termWeakness= State()
    user_numbness= State()
    user_visionLoss= State()
    user_cough= State()
    user_wheezing= State()
    user_hemoptysis= State()
    user_upperAbdomen= State()
    user_poop= State()
    user_lostWeight= State()
    user_holes= State()
    user_bleeding= State()
    user_smoke = State() # да нет
    user_howManySmoke = State() #сколько сиг/день
    user_walking = State()
    user_diet= State()
    user_addSomeSalt= State()
    user_narcotic= State()
    user_quantityAlcoholic= State()
    user_youUseAlcoholic= State()
    user_totalPoints= State()
    user_countPoints = State()
    user_otherComplaints= State()