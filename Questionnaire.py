import re
import asyncio
import json
import sqlite3 as sq
import os
from aiogram import types
from os import getenv
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from Form import Form
from aiogram.fsm.state import StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from keys import Keys
from aiogram.filters import Command

# from yadisk import YaDisk
from dotenv import load_dotenv
from Inserter import DataInserter
from Tables import MyTables
from datetime import date

class listQuestions(StatesGroup):
    forwardButton: str = "Вперед"
    changeButton: str = "Изменить"
    historyOutputButton: str = "Вывод анкеты"
    exitMainMenuButton: str = "Выход в главное меню"
    
    def __init__(self,TOKEN,dp,Router):
        self.dp = dp
        self.TOKEN = TOKEN
        self.bot = getenv(self.TOKEN)
        self.Router = Router
        
    def survey(self):
        @self.dp.callback_query(F.data == "menu1")
        async def command_start(callback_query: types.CallbackQuery, state: FSMContext):
           
            text="1.1) (Введите с клавиатуры) Ф.И.О."
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="survey1.2")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="menu1")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1,button2,button3,button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_name)
            
            
        @self.dp.message(Command("questionnaire"))
        async def command_start(message: types.Message, state: FSMContext):
            
            text="1.1) (Введите с клавиатуры) Ф.И.О."
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="survey1.2")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="menu1")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1,button2,button3,button4)
            builder.adjust(2)
            await message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_name)
            

        @self.dp.message(Form.user_name)
        async def user_name(message: Message, state: FSMContext):
            
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_name=message.text)
                  
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
            
            
        # ####################################################################################################################################

        @self.dp.callback_query(F.data == "survey1.2")
        async def user_passport(callback_query:types.CallbackQuery, state: FSMContext):
            text="1.2) (Введите с клавиатуры) Пастпортные данные (серия, номер)" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="survey1.3")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey1.2")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_passport)

        @self.dp.message(Form.user_passport)
        async def user_passport(message: Message, state: FSMContext):
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_passport=message.text) 
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
            

        
        @self.dp.callback_query(F.data == "survey1.3")
        async def user_city(callback_query:types.CallbackQuery, state: FSMContext):
            text="1.3) (Введите с клавиатуры) Город проживания" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="survey1.4")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey1.3")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_city)

        @self.dp.message(Form.user_city)
        async def user_city(message: Message, state: FSMContext):
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_city=message.text)
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
            

        # ####################################################################################################################################
        @self.dp.callback_query(F.data == "survey1.4")
        async def user_address(callback_query: types.CallbackQuery, state: FSMContext):
            text="1.4) (Введите с клавиатуры) Адресс проживания" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="survey1.5")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey1.4")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_address)

        @self.dp.message(Form.user_address)
        async def user_address(message: Message, state: FSMContext):
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_address=message.text) 
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")            

        @self.dp.callback_query(F.data == "survey1.5")
        async def user_telephone(callback_query: types.CallbackQuery, state: FSMContext):
            text="1.5) (Введите с клавиатуры) Контактный телефон" 
            builder = InlineKeyboardBuilder() 
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="survey2")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey1.3")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_telephone)

        @self.dp.message(Form.user_telephone)
        async def user_telephone(message: Message, state: FSMContext):
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_telephone=message.text) 
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
            

        @self.dp.callback_query(F.data == "survey2")
        async def user_gender(callback_query: types.CallbackQuery, state: FSMContext):
            text="2) (Введите с клавиатуры) Пол (Пример:м/ж)" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="survey3")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey2")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_gender)

        @self.dp.message(Form.user_gender)
        async def user_gender(message: Message, state: FSMContext):
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_gender=message.text)
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
        
        @self.dp.callback_query(F.data == "survey3")
        async def user_age(callback_query: types.CallbackQuery, state: FSMContext):
            text="3) (Введите с клавиатуры) Возраст" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="survey4")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey3")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_age)

        @self.dp.message(Form.user_age)
        async def user_age(message: Message, state: FSMContext):
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_age=message.text)
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
            

        @self.dp.callback_query(F.data == "survey4")
        async def user_height(callback_query: types.CallbackQuery, state: FSMContext):
            text="4) (Введите с клавиатуры) Рост" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="survey5")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey4")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_height)

        @self.dp.message(Form.user_height)
        async def user_height(message: Message, state: FSMContext):
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_height=message.text)
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
            
       
        @self.dp.callback_query(F.data == "survey5")
        async def user_weight(callback_query: types.CallbackQuery, state: FSMContext):
            text="5) (Введите с клавиатуры) Вес" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="survey6")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey5")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_weight)

        @self.dp.message(Form.user_weight)
        async def user_weight(message: Message, state: FSMContext):
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_weight=message.text)
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
            
        
        @self.dp.callback_query(F.data == "survey6")
        async def user_briefDescriptionComplaintsDate(callback_query: types.CallbackQuery, state: FSMContext):
            text="6) (Введите с клавиатуры) Краткое описание жалоб на данный момент" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="survey7")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey6")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_briefDescriptionComplaintsDate)

        @self.dp.message(Form.user_briefDescriptionComplaintsDate)
        async def user_briefDescriptionComplaintsDate(message: Message, state: FSMContext):
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_briefDescriptionComplaintsDate=message.text)
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
            
        
        @self.dp.callback_query(F.data == "survey7")
        async def user_allergicReactions(callback_query: types.CallbackQuery, state: FSMContext):
            text="7) (Введите с клавиатуры) Аллергические реакции" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="survey8.1")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey7")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_allergicReactions)

        @self.dp.message(Form.user_allergicReactions)
        async def user_allergicReactions(message: Message, state: FSMContext):
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_allergicReactions=message.text)
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
           
#########################################################################################################################################
        @self.dp.callback_query(F.data == "survey8.1")
        async def user_hyperallergicReactionstonicDisease(callback_query: types.CallbackQuery, state: FSMContext):
            listQuestions.tF = False
            text="8.1) Гипертоническая болезнь(повышенное артериальное давление) да/нет?" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="Yes")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="No1")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey8.1")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")  
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_hyperallergicReactionstonicDisease)

        @self.dp.callback_query(F.data == "Yes")
        async def user_takeHyperallergicMedications(callback_query: types.CallbackQuery, state: FSMContext):
            listQuestions.tF = True
            text="8.1) Принимаете ли Вы препараты для снижения давления? Напишите (да/нет) Если (да), то какие? (Введите с клавиатуры)" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="survey8.2")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="Yes")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_takeHyperallergicMedications)
            await state.update_data(user_hyperallergicReactionstonicDisease="Да")

        @self.dp.message(Form.user_takeHyperallergicMedications)
        async def user_takeHyperallergicMedications(message: Message, state: FSMContext):
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_takeHyperallergicMedications=message.text)
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
            
        
 
        @self.dp.callback_query(lambda c: re.match("(survey8.2|No1)", c.data))
        async def user_cardiacIschemia(callback_query: types.CallbackQuery, state: FSMContext):
            if (listQuestions.tF == False):
                data = await state.get_data()
                await state.set_data(data)
                await state.set_state(Form.user_hyperallergicReactionstonicDisease)
                await state.update_data(user_hyperallergicReactionstonicDisease="Нет")
                await state.set_state(Form.user_takeHyperallergicMedications)
                await state.update_data(user_takeHyperallergicMedications = "---")
                
                
            
            text="8.2) Ишемическая болезнь сердца (стенокардия)? да/нет?" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= "Да", callback_data="survey8Yes4")
            button5 = types.InlineKeyboardButton(text= "Нет", callback_data="survey8No4")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey8.2|No1")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1,button5, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_cardiacIschemia)
                   
########################################################################################################## 
        @self.dp.callback_query(lambda c: re.match("(survey8Yes4|survey8No4)", c.data))
        async def user_cerebrovascularDisease(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "survey8Yes4":
                await state.update_data(user_cardiacIschemia="Да")
            elif callback_query.data == "survey8No4":
                await state.update_data(user_cardiacIschemia="Нет")
            await callback_query.answer()

            text="8.3) Цереброваскулярное заболевание (заболевание сосудов головногомозга)? да/нет?" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="Survey8Yes5")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="Survey8No5")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey8Yes4|survey8No4")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_cerebrovascularDisease)
            
        @self.dp.callback_query(lambda c: re.match("(Survey8Yes5|Survey8No5)", c.data))
        async def user_chronicDisease(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "Survey8Yes5":
                await state.update_data(user_cerebrovascularDisease="Да")
            elif callback_query.data == "Survey8No5":
                await state.update_data(user_cerebrovascularDisease="Нет")
            await callback_query.answer()

            text="8.4) Хроническое заболевание бронхов или легких (хронический бронхит, эмфизема, бронхиальная астма)? да/нет?" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="Survey8Yes6")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="Survey8No6")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="Survey8Yes5|Survey8No5")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_chronicDisease)
        
        @self.dp.callback_query(lambda c: re.match("(Survey8Yes6|Survey8No6)", c.data))
        async def user_tuberculosis(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "Survey8Yes6":
                await state.update_data(user_chronicDisease="Да")
            elif callback_query.data == "Survey8No6":
                await state.update_data(user_chronicDisease="Нет")
            await callback_query.answer()

            text="8.5) Туберкулез (легких или иных локализаций)? да/нет?" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="Survey8Yes7")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="Survey8No7")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="Survey8Yes6|Survey8No6")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_tuberculosis)
        
        @self.dp.callback_query(lambda c: re.match("(Survey8Yes7|Survey8No7)", c.data))
        async def user_diabetes(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "Survey8Yes7":
                await state.update_data(user_tuberculosis="Да")
            elif callback_query.data == "Survey8No7":
                await state.update_data(user_tuberculosis="Нет")
            await callback_query.answer()
            
            listQuestions.tF = False
            text="8.6) Сахарный диабет или повышенный уровень сахара в крови? да/нет?" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="Survey8Yes8")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="Survey8No8")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="Survey8Yes7|Survey8No7")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_diabetes)

        @self.dp.callback_query(F.data == "Survey8Yes8")
        async def user_diabetes(callback_query: types.CallbackQuery, state: FSMContext):
            listQuestions.tF = True
            
            text="8.6) Принимаете ли Вы препараты для снижения уровня сахара? Напишите (да/нет) Если (да), то какие? (Введите с клавиатуры)" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="survey8.6")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="Survey8Yes8")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_takeMedications)
            await state.update_data(user_diabetes="Да")

        @self.dp.message(Form. user_takeMedications)
        async def  user_takeMedications(message: Message, state: FSMContext):
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_takeMedications=message.text)
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
            
 
        @self.dp.callback_query(lambda c: re.match("(survey8.6|Survey8No8)", c.data))
        async def user_diabetes(callback_query: types.CallbackQuery, state: FSMContext):
            if (listQuestions.tF == False):
                data = await state.get_data()
                await state.set_data(data)
                await state.set_state(Form.user_diabetes)
                await state.update_data(user_diabetes="Нет")
                await state.set_state(Form.user_takeMedications)
                await state.update_data(user_takeMedications = "---") 
                
               
            
            text="8.7) Заболевания желудка (гастрит, язвенная болезнь)? да/нет" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= "Да", callback_data="survey8Yes9")
            button5 = types.InlineKeyboardButton(text= "Нет", callback_data="survey8No9")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey8.6|Survey8No8")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1,button5, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_stomachDiseases)
        
        @self.dp.callback_query(lambda c: re.match("(survey8Yes9|survey8No9)", c.data))
        async def user_stomachDiseases(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "survey8Yes9":
                await state.update_data(user_stomachDiseases= "Да")
            elif callback_query.data == "survey8No9":
                await state.update_data(user_stomachDiseases= "Нет")
            await callback_query.answer()
            
            text="8.8) Хроническое заболевание почек? да/нет" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="Survey8Yes10")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="Survey8No10")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey8Yes9|survey8No9")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_chronicKidneyDisease)
        
        @self.dp.callback_query(lambda c: re.match("(Survey8Yes10|Survey8No10)", c.data))
        async def user_chronicKidneyDisease(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "Survey8Yes10":
                await state.update_data(user_chronicKidneyDisease= "Да")
            elif callback_query.data == "Survey8No10":
                await state.update_data(user_chronicKidneyDisease= "Нет")
            await callback_query.answer()
            
            listQuestions.tF = False
            text="8.9) Злокачественное новообразование? да/нет" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="Survey8Yes11")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="Survey8No11")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="Survey8Yes10|Survey8No10")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_malignantNeoplasm)

        @self.dp.callback_query(F.data == "Survey8Yes11")
        async def user_whichMalignantNeoplasm(callback_query: types.CallbackQuery, state: FSMContext):
        
            listQuestions.tF = True
            text="8.9) Какое злокачественное новообразование? Напишите (да/нет) Если (да), то какие? (Введите с клавиатуры)" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="Survey8Yes12")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="Survey8Yes11")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            
            await state.update_data(user_malignantNeoplasm="Да")
            await state.set_state(Form.user_whichMalignantNeoplasm)
            
        @self.dp.message(Form.user_whichMalignantNeoplasm)
        async def  user_whichMalignantNeoplasm(message: Message, state: FSMContext):      
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_whichMalignantNeoplasm=message.text)
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
            
 
        @self.dp.callback_query(lambda c: re.match("(Survey8Yes12|Survey8No11)", c.data))
        async def user_diabetes(callback_query: types.CallbackQuery, state: FSMContext):
            if (listQuestions.tF == False):
                data = await state.get_data()
                await state.set_data(data)
                await state.set_state(Form.user_malignantNeoplasm)
                await state.update_data(user_malignantNeoplasm="Нет")
                await state.set_state(Form.user_whichMalignantNeoplasm)
                await state.update_data(user_whichMalignantNeoplasm = "---")
                
            listQuestions.tF = False
            text="8.10) Повышенный уровень холестерина? да/нет" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= "Да", callback_data="survey8Yes13")
            button5 = types.InlineKeyboardButton(text= "Нет", callback_data="survey8No13")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="Survey8Yes12|Survey8No11")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1,button5, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_elevatedСholesterol)
        
        @self.dp.callback_query(F.data == "survey8Yes13")
        async def user_elevatedСholesterol(callback_query: types.CallbackQuery, state: FSMContext):
            listQuestions.tF = True
            text="8.10) Принимаете ли Вы препараты для снижения уровня холестерина? Напишите (да/нет) Если (да), то какие? (Введите с клавиатуры)" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="Survey8Yes14")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="Survey8Yes13")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_drugsElevatedСholesterol)
            await state.update_data(user_elevatedСholesterol="Да")

        @self.dp.message(Form. user_drugsElevatedСholesterol)
        async def  user_drugsElevatedСholesterol(message: Message, state: FSMContext):
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_drugsElevatedСholesterol=message.text)
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
            
 
        @self.dp.callback_query(lambda c: re.match("(Survey8Yes14|survey8No13)", c.data))
        async def user_drugsElevatedСholesterol(callback_query: types.CallbackQuery, state: FSMContext):
            if (listQuestions.tF == False):
                data = await state.get_data()
                await state.set_data(data)
                await state.set_state(Form.user_elevatedСholesterol)
                await state.update_data(user_elevatedСholesterol="Нет")
                await state.set_state(Form.user_drugsElevatedСholesterol)
                await state.update_data(user_drugsElevatedСholesterol = "---")                                
            
            text="9) Был ли у Вас инфаркт миокарда? да/нет" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= "Да", callback_data="survey9Yes")
            button5 = types.InlineKeyboardButton(text= "Нет", callback_data="survey9No")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="Survey8Yes14|survey8No13")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1,button5, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_myocardium)
        
        @self.dp.callback_query(lambda c: re.match("(survey9Yes|survey9No)", c.data))
        async def user_myocardium(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "survey9Yes":
                await state.update_data(user_myocardium= "Да")
            elif callback_query.data == "survey9No":
                await state.update_data(user_myocardium= "Нет")
            await callback_query.answer()
            
            
            text="10) Был ли у Вас инсульт? да/нет" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="Survey10Yes")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="Survey10No")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey9Yes|survey9No")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_stroke)

        @self.dp.callback_query(lambda c: re.match("(Survey10Yes|Survey10No)", c.data))
        async def user_stroke(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "Survey10Yes":
                await state.update_data(user_stroke= "Да")
            elif callback_query.data == "Survey10No":
                await state.update_data(user_stroke= "Нет")
            await callback_query.answer()
            
            
            text="""11) Был ли инфаркт миокарда или инсульт у Ваших близких
родственников в молодом или среднем возрасте (до 65 лет у
матери или родных сестер или до 55 лет у отца или родных братьев)? да/нет""" 

            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="Survey11Yes")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="Survey11No")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="Survey10Yes|Survey10No")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_myocardialInfarction)

        @self.dp.callback_query(lambda c: re.match("(Survey11Yes|Survey11No)", c.data))
        async def user_myocardialInfarction(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "Survey11Yes":
                await state.update_data(user_myocardialInfarction = "Да")
            elif callback_query.data == "Survey11No":
                await state.update_data(user_myocardialInfarction = "Нет")
            await callback_query.answer()            
            
            text="""12) Были ли у Ваших близких родственников в молодом или
среднем возрасте злокачественные новообразования (легкого,
желудка, кишечника, толстой или прямой кишки, предстательной
железы, молочной железы, матки, опухоли других локализаций) или
полипоз желудка, семейный аденоматоз / диффузный полипоз
толстой кишки? да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="Survey13Yes")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="Survey13No")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="Survey11Yes|Survey11No")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button5,button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_Relatives)
        
        

        
        @self.dp.callback_query(lambda c: re.match("(Survey13Yes|Survey13No)", c.data))
        async def user_chestDiscomfort(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "Survey13Yes":
                await state.update_data(user_Relatives= "Да")
            elif callback_query.data == "Survey13No":
                await state.update_data(user_Relatives= "Нет")
            await callback_query.answer()

            listQuestions.tF = False
            text="""13) Возникает ли у Вас, когда поднимаетесь по лестнице, идете в гору или спешите, или при выходе из теплого помещения на холодный воздух, боль или ощущение давления, жжения, тяжести или явного дискомфорта за грудиной и (или) в левой половине грудной клетки, и (или) в левом плече, и (или) в левой руке? да/нет"""    
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes13")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo13")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="Survey13Yes")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_chestDiscomfort)

        @self.dp.callback_query(F.data == "SurveyYes13")
        async def user_chestDiscomfort(callback_query: types.CallbackQuery, state: FSMContext):
            listQuestions.tF = True
            text="""14) Если на вопрос 6 ответ «Да», то указанные
боли/ощущения/дискомфорт исчезают сразу или в течение не
более чем 20 мин после прекращения ходьбы/адаптации к
холоду/ в тепле/в покое и (или) они исчезают через 1−5 мин после
приема нитроглицерина (Введите с клавиатуры)""" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="SurveyYes14")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes13")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.update_data(user_chestDiscomfort="Да")
            await state.set_state(Form.user_ifChestDiscomfort)
            
        @self.dp.message(Form. user_ifChestDiscomfort)
        async def  user_ifChestDiscomfort(message: Message, state: FSMContext):
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_ifChestDiscomfort=message.text)
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
            
 
        @self.dp.callback_query(lambda c: re.match("(SurveyYes14|SurveyNo13)", c.data))
        async def user_termWeakness(callback_query: types.CallbackQuery, state: FSMContext):
            if (listQuestions.tF == False):
                data = await state.get_data()
                await state.set_data(data)
                await state.set_state(Form.user_chestDiscomfort)
                await state.update_data(user_chestDiscomfort="Нет")
                await state.set_state(Form.user_ifChestDiscomfort)
                await state.update_data(user_ifChestDiscomfort = "---")
                        
            text="""15) Возникала ли у Вас когда-либо внезапная кратковременная слабость или неловкость при движении в одной руке (ноге) либо руке и ноге одновременно так, что Вы не могли взять или удержать предмет, встать со стула, пройтись по комнате?  да/нет""" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= "Да", callback_data="surveyYes15")
            button5 = types.InlineKeyboardButton(text= "Нет", callback_data="surveyNo15")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes14|SurveyNo13")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1,button5, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_termWeakness)
        
        @self.dp.callback_query(lambda c: re.match("(surveyYes15|surveyNo15)", c.data))
        async def user_termWeakness(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "surveyYes15":
                await state.update_data(user_termWeakness= "Да")
            elif callback_query.data == "surveyNo15":
                await state.update_data(user_termWeakness= "Нет")
            await callback_query.answer()
            
            text="""16) Возникало ли у Вас когда-либо внезапное без явных причин кратковременное онемение в одной руке, ноге или половине лица, губы или языка? да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes16")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo16")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="surveyYes15|surveyNo15")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_numbness)
        
        @self.dp.callback_query(lambda c: re.match("(SurveyYes16|SurveyNo16)", c.data))
        async def user_numbness(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyYes16":
                await state.update_data(user_numbness= "Да")
            elif callback_query.data == "SurveyNo16":
                await state.update_data(user_numbness= "Нет")
            await callback_query.answer()
            
            
            text="""17) Возникала ли у Вас когда-либо внезапно кратковременная потеря зрения на один глаз? да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes17")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo17")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes16|SurveyNo16")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_visionLoss)
        


        @self.dp.callback_query(lambda c: re.match("(SurveyYes17|SurveyNo17)", c.data))
        async def user_visionLoss(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyYes17":
                await state.update_data(user_visionLoss= "Да")
            elif callback_query.data == "SurveyNo17":
                await state.update_data(user_visionLoss= "Нет")
            await callback_query.answer()
            
            text="""18) Бывают ли у Вас ежегодно периоды ежедневного кашля с отделением мокроты на протяжении примерно 3 месяцев в году? да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes18")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo18")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes17|SurveyNo17")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_cough)

        

        @self.dp.callback_query(lambda c: re.match("(SurveyYes18|SurveyNo18)", c.data))
        async def user_cough(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyYes18":
                await state.update_data(user_cough= "Да")
            elif callback_query.data == "SurveyNo18":
                await state.update_data(user_cough= "Нет")
            await callback_query.answer()
            
            
            text="""19) Бывают ли у Вас свистящие или жужжащие хрипы в грудной клетке при дыхании, не проходящие при откашливании? да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes19")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo19")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes18|SurveyNo18")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_wheezing)
        
        @self.dp.callback_query(lambda c: re.match("(SurveyYes19|SurveyNo19)", c.data))
        async def user_wheezing(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyYes19":
                await state.update_data(user_wheezing= "Да")
            elif callback_query.data == "SurveyNo19":
                await state.update_data(user_wheezing= "Нет")
            await callback_query.answer()
            
            
            text="""20) Бывало ли у Вас когда-либо кровохарканье? да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes20")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo20")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes19|SurveyNo19")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_hemoptysis)
        
        @self.dp.callback_query(lambda c: re.match("(SurveyYes20|SurveyNo20)", c.data))
        async def user_hemoptysis(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyYes20":
                await state.update_data(user_hemoptysis= "Да")
            elif callback_query.data == "SurveyNo20":
                await state.update_data(user_hemoptysis= "Нет")
            await callback_query.answer()
            
            
            text="""21) Беспокоят ли Вас боли в области верхней части живота (в области желудка), отрыжка, тошнота, рвота, ухудшение или отсутствие аппетита? да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes21")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo21")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes20|SurveyNo20")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_upperAbdomen)
        
        @self.dp.callback_query(lambda c: re.match("(SurveyYes21|SurveyNo21)", c.data))
        async def user_upperAbdomen(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyYes21":
                await state.update_data(user_upperAbdomen= "Да")
            elif callback_query.data == "SurveyNo21":
                await state.update_data(user_upperAbdomen= "Нет")
            await callback_query.answer()
            
            
            text="""22) Бывает ли у Вас неоформленный (полужидкий) черный или дегтеобразный стул? да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes22")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo22")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes21|SurveyNo21")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_poop)
        
        @self.dp.callback_query(lambda c: re.match("(SurveyYes22|SurveyNo22)", c.data))
        async def user_poop(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyYes22":
                await state.update_data(user_poop= "Да")
            elif callback_query.data == "SurveyNo22":
                await state.update_data(user_poop= "Нет")
            await callback_query.answer()
            
            
            text="""23) Похудели ли Вы за последнее время без видимых причин (т.е. без соблюдения диеты или увеличения физической активности и пр.)? да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes23")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo23")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes22|SurveyNo22")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_lostWeight)
        
        @self.dp.callback_query(lambda c: re.match("(SurveyYes23|SurveyNo23)", c.data))
        async def user_lostWeight(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyYes23":
                await state.update_data(user_lostWeight= "Да")
            elif callback_query.data == "SurveyNo23":
                await state.update_data(user_lostWeight= "Нет")
            await callback_query.answer()
            
            
            text="""24)  Бывает ли у Вас боль в области заднепроходного отверстия? да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes24")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo24")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes23|SurveyNo23")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_holes)
        
        @self.dp.callback_query(lambda c: re.match("(SurveyYes24|SurveyNo24)", c.data))
        async def user_holes(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyYes24":
                await state.update_data(user_holes= "Да")
            elif callback_query.data == "SurveyNo24":
                await state.update_data(user_holes= "Нет")
            await callback_query.answer()
            
            
            text="""25) Бывают ли у Вас кровяные выделения с калом? да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes25")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo25")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes24|SurveyNo24")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_bleeding)
        
        @self.dp.callback_query(lambda c: re.match("(SurveyYes25|SurveyNo25)", c.data))
        async def user_bleeding(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyYes25":
                await state.update_data(user_bleeding= "Да")
            elif callback_query.data == "SurveyNo25":
                await state.update_data(user_bleeding= "Нет")
            await callback_query.answer()
            
            listQuestions.tF = False
            text="""26) Курите ли Вы? (курение одной и более сигарет в день) да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes26")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo26")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes25|SurveyNo25")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_smoke)

        @self.dp.callback_query(F.data == "SurveyYes26")
        async def user_smoke(callback_query: types.CallbackQuery, state: FSMContext):
            listQuestions.tF = True
            text="27) Если Вы курите, то сколько в среднем сигарет в день выкуриваете? ___________ сиг/день (Введите с клавиатуры)" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="SurveyYes27")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes26")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.update_data(user_smoke="Да")
            await state.set_state(Form.user_howManySmoke)
            
        @self.dp.message(Form.user_howManySmoke)
        async def user_howManySmoke(message: Message, state: FSMContext):
            if  not message.text:
                await message.answer("Ошибка")
                await message.delete()
                return
            
            elif message.text.startswith('/'):
                return
            
            MAX_CHARACTERS = 1000
            
            if len(message.text) <= MAX_CHARACTERS:    
                await state.update_data(user_howManySmoke=message.text)
            else:
                await message.answer(f"Пожалуйста, введите не более {MAX_CHARACTERS} символов.")
           
 
        @self.dp.callback_query(lambda c: re.match("(SurveyYes27|SurveyNo26)", c.data))
        async def user_walking(callback_query: types.CallbackQuery, state: FSMContext):
            if (listQuestions.tF == False):
                data = await state.get_data()
                await state.set_data(data)
                await state.set_state(Form.user_smoke)
                await state.update_data(user_smoke="Нет")
                await state.set_state(Form.user_howManySmoke)
                await state.update_data(user_howManySmoke = "---")
                
            text="""28) Сколько минут в день Вы тратите на ходьбу в умеренном или быстром темпе (включая дорогу до места работы и обратно)? До 30 минут 30 минут и более да/нет""" 
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes28")
            button5 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo28")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes27|SurveyNo26")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1,button5, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_walking)
        

        @self.dp.callback_query(lambda c: re.match("(SurveyYes28|SurveyNo28)", c.data))
        async def user_diet(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyYes28":
                await state.update_data(user_walking= "Да")
            elif callback_query.data == "SurveyNo28":
                await state.update_data(user_walking= "Нет")
            await callback_query.answer()
            
            
            text="""29) Присутствует ли в Вашем ежедневном рационе 400−500 г сырых овощей и фруктов? да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes29")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo29")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes28|SurveyNo28")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_diet)
        
        @self.dp.callback_query(lambda c: re.match("(SurveyYes29|SurveyNo29)", c.data))
        async def user_addSomeSalt(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyYes29":
                await state.update_data(user_diet= "Да")
            elif callback_query.data == "SurveyNo29":
                await state.update_data(user_diet= "Нет")
            await callback_query.answer()
            
            text="""30) Имеете ли Вы привычку подсаливать приготовленную пищу, не пробуя ее? да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes30")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo30")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes29|SurveyNo29")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_addSomeSalt)
        
        @self.dp.callback_query(lambda c: re.match("(SurveyYes30|SurveyNo30)", c.data))
        async def user_narcotic(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyYes30":
                await state.update_data(user_addSomeSalt= "Да")
            elif callback_query.data == "SurveyNo30":
                await state.update_data(user_addSomeSalt= "Нет")
            await callback_query.answer()
            
            text="""31) Принимали ли Вы за последний год психотропные или наркотические вещества без назначения врача? да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes31")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo31")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes30|SurveyNo30")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_narcotic)
        
        @self.dp.callback_query(lambda c: re.match("(SurveyYes31|SurveyNo31)", c.data))
        async def user_quantityAlcoholic(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyYes31":
                await state.update_data(user_narcotic= "Да")
            elif callback_query.data == "SurveyNo31":
                await state.update_data(user_narcotic= "Нет")
            await callback_query.answer()
            
            text="""32) Как часто Вы употребляете алкогольные напитки? (Выберите ответ из предложенных вариантов)""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Никогда", callback_data="SurveyNever32")
            button6 = types.InlineKeyboardButton(text= "Раз в месяц и реже", callback_data="SurveyOnceMonth32")
            button7 = types.InlineKeyboardButton(text= "2−4 раза в месяц", callback_data="SurveyA32")
            button8 = types.InlineKeyboardButton(text= "2−3 раза в неделю", callback_data="SurveyB32")
            button9 = types.InlineKeyboardButton(text= "≥ 4 раз в неделю", callback_data="SurveyC32")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyYes31|SurveyNo31")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button7, button8, button9, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_quantityAlcoholic)
        
        @self.dp.callback_query(lambda c: re.match("(SurveyNever32|SurveyOnceMonth32|SurveyA32|SurveyB32|SurveyC32)", c.data))
        async def user_youUseAlcoholic(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyNever32":
                await state.update_data(user_quantityAlcoholic= 0)
            elif callback_query.data == "SurveyOnceMonth32":
                await state.update_data(user_quantityAlcoholic= 1)
            elif callback_query.data == "SurveyA32":
                await state.update_data(user_quantityAlcoholic= 2)
            elif callback_query.data == "SurveyB32":
                await state.update_data(user_quantityAlcoholic= 3)
            elif callback_query.data == "SurveyC32":
                await state.update_data(user_quantityAlcoholic= 4)
            await callback_query.answer()
            
            text="""33) Какое количество алкогольных напитков (порций) Вы выпиваете обычно за один раз? 1 порция равна 12 мл чистого этанола ИЛИ 30 мл крепкого алкоголя (водки), ИЛИ 100 мл сухого вина, ИЛИ 300 мл пива (Выберите ответ из предложенных вариантов)""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "1−2 порции", callback_data="SurveyNever33")
            button6 = types.InlineKeyboardButton(text= "3−4 порции", callback_data="SurveyOnceMonth33")
            button7 = types.InlineKeyboardButton(text= "5−6 порций", callback_data="SurveyA33")
            button8 = types.InlineKeyboardButton(text= "7−9 порций", callback_data="SurveyB33")
            button9 = types.InlineKeyboardButton(text= "≥ 10 порций", callback_data="SurveyC33")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyNever32|SurveyOnceMonth32|SurveyA32|SurveyB32|SurveyC32")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button7, button8, button9, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_youUseAlcoholic)
        
        @self.dp.callback_query(lambda c: re.match("(SurveyNever33|SurveyOnceMonth33|SurveyA33|SurveyB33|SurveyC33)", c.data))
        async def user_totalPoints(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyNever33":
                await state.update_data(user_youUseAlcoholic= 0)
            elif callback_query.data == "SurveyOnceMonth33":
                await state.update_data(user_youUseAlcoholic= 1)
            elif callback_query.data == "SurveyA33":
                await state.update_data(user_youUseAlcoholic= 2)
            elif callback_query.data == "SurveyB33":
                await state.update_data(user_youUseAlcoholic= 3)
            elif callback_query.data == "SurveyC33":
                await state.update_data(user_youUseAlcoholic= 4)
            await callback_query.answer()
                        
            text="""34) Как часто Вы употребляете за один раз 6 или более порций? 6 порций равны ИЛИ 180 мл крепкого алкоголя (водки), ИЛИ 600 мл сухого вина, ИЛИ 1,8 л пива (Выберите ответ из предложенных вариантов)""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Никогда", callback_data="SurveyNever34")
            button6 = types.InlineKeyboardButton(text= "Раз в месяц и реже", callback_data="SurveyOnceMonth34")
            button7 = types.InlineKeyboardButton(text= "2-4 раза в месяц", callback_data="SurveyA34")
            button8 = types.InlineKeyboardButton(text= "2−3 раза в неделю", callback_data="SurveyB34")
            button9 = types.InlineKeyboardButton(text= "≥ 4 раз в неделю", callback_data="SurveyC34")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyNever33|SurveyOnceMonth33|SurveyA33|SurveyB33|SurveyC33")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button7, button8, button9, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_totalPoints)

        @self.dp.callback_query(lambda c: re.match("(SurveyNever34|SurveyOnceMonth34|SurveyA34|SurveyB34|SurveyC34)", c.data))
        async def user_otherComplaints(callback_query: types.CallbackQuery, state: FSMContext):
            if callback_query.data == "SurveyNever34":
                await state.update_data(user_totalPoints= 0)
            elif callback_query.data == "SurveyOnceMonth34":
                await state.update_data(user_totalPoints= 1)
            elif callback_query.data == "SurveyA34":
                await state.update_data(user_totalPoints= 2)
            elif callback_query.data == "SurveyB34":
                await state.update_data(user_totalPoints= 3)
            elif callback_query.data == "SurveyC34":
                await state.update_data(user_totalPoints= 4)
            await callback_query.answer()

            await state.set_state(Form.user_countPoints)
            r_data = await state.get_data() 

            summa = r_data.get("user_totalPoints",0) + r_data.get("user_youUseAlcoholic",0) + r_data.get("user_quantityAlcoholic",0)
            
            await state.update_data(user_countPoints = summa)

            text=f"35) ОБЩАЯ СУММА БАЛЛОВ в ответах на вопросы №32-34 равна {summa} баллов (Нажмите кнопку 'вперед')"
            
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text= listQuestions.forwardButton, callback_data="survey36")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="SurveyNever33|SurveyOnceMonth33|SurveyA33|SurveyB33|SurveyC33")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog")
            builder.add(button1, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_otherComplaints)

        @self.dp.callback_query(F.data == "survey36")
        async def user_otherComplaints(callback_query: types.CallbackQuery, state: FSMContext):
            
            text="""36) Есть ли у Вас другие жалобы на свое здоровье, не вошедшие в настоящую анкету и которые Вы бы хотели сообщить врачу (фельдшеру)? да/нет""" 
            builder = InlineKeyboardBuilder()
            button5 = types.InlineKeyboardButton(text= "Да", callback_data="SurveyYes36")
            button6 = types.InlineKeyboardButton(text= "Нет", callback_data="SurveyNo36")
            button2 = types.InlineKeyboardButton(text= listQuestions.changeButton, callback_data="survey36")
            button3 = types.InlineKeyboardButton(text= listQuestions.historyOutputButton, callback_data="anamnesis")
            button4 = types.InlineKeyboardButton(text= listQuestions.exitMainMenuButton, callback_data="Catalog") 
            builder.add(button5, button6, button2, button3, button4)
            builder.adjust(2)
            await callback_query.message.answer(text,reply_markup=builder.as_markup())
            await state.set_state(Form.user_otherComplaints)
        
        @self.dp.callback_query(lambda c: re.match("(anamnesis|SurveyYes36|SurveyNo36)", c.data))
        async def anamnesis(callback_query: Message, state: FSMContext):
            if callback_query.data == "SurveyYes36":
                await state.update_data(user_otherComplaints = "Да")
            elif callback_query.data == "SurveyNo36":
                await state.update_data(user_otherComplaints = "Нет")

            user_data = await state.get_data()
            if not user_data: 
                await callback_query.message.answer(
                    text="Анкета не заполнена",
                )
                return
            
            user_data = json.dumps(user_data, indent=4, ensure_ascii=False)

            correctKeys = Keys(user_data)
            user_data = correctKeys.changingKeys()

            with open("Questionnaire.txt", 'w', encoding='utf-8') as file:
                file.write(user_data)

            builder = InlineKeyboardBuilder()
            button = types.InlineKeyboardButton(text="Сохранить", callback_data="save")
            builder.add(button)
            builder.adjust(1)

            user_data_str = user_data
            user_data_parts = [user_data_str[i:i + 4000] for i in range(0, len(user_data_str), 4000)]  

            for part in user_data_parts:
                await callback_query.message.answer(text=f"<pre>{part}</pre>", parse_mode="HTML", reply_markup=builder.as_markup())
           

        @self.dp.callback_query(F.data == "save")
        async def save(callback_query: Message, state: FSMContext): 
            text2 = "Перед сохронением убедитесь что все поля данных заполнены"
            builder = InlineKeyboardBuilder()
            button = types.InlineKeyboardButton(text="Сохранить всю анкету", callback_data="mainSave")
            builder.add(button)
            builder.adjust(1)
            await callback_query.message.answer(text2,reply_markup=builder.as_markup())

        @self.dp.callback_query(F.data == "mainSave")
        async def mainSave(callback_query: types.Message, state: FSMContext):
            async def save_data():
                user_data = await state.get_data()
                countValue = len(user_data)

                if countValue >= 47:
                    db_path = 'mydatabase.db'

                    with sq.connect(db_path) as con:
                        tables_creator = MyTables(con)
                        tables_creator.sql_tables()

                    today = date.today()
                    
                    patient_data = await state.get_data()

                    inserter = DataInserter(con)
                    inserter.insert_data(patient_data.get("user_name", 0), patient_data.get("user_passport", 0),
                                        patient_data.get("user_city", 0), patient_data.get("user_address",0),
                                        patient_data.get("user_telephone",0), patient_data.get("user_gender", 0),
                                        f"{today.day}.{today.month}.{today.year}", 
                                        patient_data.get("user_age", 0),patient_data.get("user_height", 0),patient_data.get("user_weight", 0),
                                        patient_data.get("user_briefDescriptionComplaintsDate",0),patient_data.get("user_allergicReactions",0),patient_data.get("user_hyperallergicReactionstonicDisease",0),
                                        patient_data.get("user_takeHyperallergicMedications",0),patient_data.get("user_cardiacIschemia",0),patient_data.get("user_cerebrovascularDisease",0),
                                        patient_data.get("user_chronicDisease",0),patient_data.get("user_tuberculosis",0),patient_data.get("user_diabetes",0),
                                        patient_data.get("user_takeMedications",0),patient_data.get("user_stomachDiseases",0),patient_data.get("user_chronicKidneyDisease",0),
                                        patient_data.get("user_malignantNeoplasm",0),patient_data.get("user_whichMalignantNeoplasm",0),patient_data.get("user_elevatedСholesterol",0),
                                        patient_data.get("user_drugsElevatedСholesterol",0),patient_data.get("user_myocardium",0),patient_data.get("user_stroke",0),
                                        patient_data.get("user_myocardialInfarction",0),patient_data.get("user_Relatives",0),patient_data.get("user_chestDiscomfort",0),
                                        patient_data.get("user_ifChestDiscomfort",0),patient_data.get("user_termWeakness",0),patient_data.get("user_numbness",0),
                                        patient_data.get("user_visionLoss",0),patient_data.get("user_cough",0),patient_data.get("user_wheezing",0),
                                        patient_data.get("user_hemoptysis",0),patient_data.get("user_upperAbdomen",0),patient_data.get("user_poop",0),
                                        patient_data.get("user_lostWeight",0),patient_data.get("user_holes",0),patient_data.get("user_bleeding",0),
                                        patient_data.get("user_smoke",0),patient_data.get("user_howManySmoke",0),patient_data.get("user_walking",0),
                                        patient_data.get("user_diet",0),patient_data.get("user_addSomeSalt",0),patient_data.get("user_narcotic",0),
                                        patient_data.get("user_quantityAlcoholic",0),patient_data.get("user_youUseAlcoholic",0),patient_data.get("user_totalPoints",0),
                                        patient_data.get("user_countPoints",0),patient_data.get("user_otherComplaints",0))
                    
                    await callback_query.message.answer("Ваша анкета успешно сохранена")

                else:
                    await callback_query.message.answer("Вы не ответили на все вопросы")

            await save_data()

        @self.dp.callback_query(F.data == "clear")
        async def clear(callback_query: Message, state: FSMContext):  
            await state.clear()
            await callback_query.message.answer(
                "Очистка анкеты выполнена" 
            )

        @self.dp.message()
        async def error(message: types.Message): 
            await message.delete()
            return
        
        
        
        
    