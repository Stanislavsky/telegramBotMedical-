import json
import asyncio as aio
import logging
import sys
import os

from aiogram.types import FSInputFile
from os import getenv
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F 
from Questionnaire import listQuestions
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from keys import Keys

class BaseBot(Bot):
    def __init__(self, BOT_TOKEN, dp, questionnaire,r):
        super().__init__(BOT_TOKEN)
        self.dp = dp
        self.BOT_TOKEN = BOT_TOKEN
        self.questionnaire = questionnaire
        self.bot = getenv(self.BOT_TOKEN)
        self.r = r

    def welcome(self):
        @self.dp.message(CommandStart())
        async def greetings(message: types.Message):
            textGreetings = f"""Здравствуйте, {message.from_user.username or message.from_user.first_name}! Вас приветствует Диспансер-Помощник.Бот Я помогу вам 
            с заполнением анкеты по диспансеризации. В дальнейшем у меня будет больше функций, которые я смогу вам предложить. Нажмите кнопку (главное меню), чтобы перейти в главное меню бота"""
            builder = InlineKeyboardBuilder()
            button = types.InlineKeyboardButton(text="Главное меню", callback_data="Catalog")
            builder.add(button)
            builder.adjust(1)
            await message.answer(textGreetings,reply_markup=builder.as_markup())
     
    def MainMenu(self):
        @self.dp.callback_query(F.data == 'Start')
        async def greetings(callback_query: types.CallbackQuery):
            textGreetings = f"""Здравствуйте, {callback_query.from_user.username or callback_query.from_user.first_name}! Вас приветствует Диспансер-Помощник.Бот Я помогу вам с заполнением анкеты по 
            диспансеризации. В дальнейшем у меня будет больше функций, которые я смогу вам предложить. Нажмите кнопку (главное меню), чтобы перейти в главное меню бота"""

            builder = InlineKeyboardBuilder()
            button = types.InlineKeyboardButton(text="Главное меню", callback_data="Catalog")
            builder.add(button)
            builder.adjust(1)
            await callback_query.message.edit_text(textGreetings,reply_markup=builder.as_markup())

        @self.dp.callback_query(F.data == "Catalog")
        async def menu(callback_query: types.CallbackQuery):
            textMenu = """Пожалуйста выберите один из вариантов:
1) Пройти анкетирование для диспансеризации 
2) Создать .txt документ пройденной анкеты для диспансеризации
3) Очистить все поля анкеты 
5) Вернуться к окну приветствия
4) Поддержка (Если вы нашли какие-то ошибки в моей работе напишите нам)"""
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text="Начать анкетирование", callback_data="menu1")
            button2 = types.InlineKeyboardButton(text="Создать .txt документ анкеты", callback_data="menu2")
            button3 = types.InlineKeyboardButton(text="Помощь", callback_data="menu3")
            button4 = types.InlineKeyboardButton(text="Назад", callback_data="Start")
            button5 = types.InlineKeyboardButton(text="Очистить все поля анкеты", callback_data="clear")
            builder.add(button1,button2,button5,button4,button3)
            builder.adjust(1)
            await callback_query.message.edit_text(textMenu,reply_markup=builder.as_markup())
            
        @self.dp.message(Command("mainmenu"))
        async def menu2(message: types.Message):
            textMenu = """Пожалуйста выберите один из вариантов:
1) Пройти анкетирование для диспансеризации 
2) Создать .txt документ пройденной анкеты для диспансеризации
3) Очистить все поля анкеты 
5) Вернуться к окну приветствия
4) Поддержка (Если вы нашли какие-то ошибки в моей работе напишите нам)"""
            builder = InlineKeyboardBuilder()
            button1 = types.InlineKeyboardButton(text="Начать анкетирование", callback_data="menu1")
            button2 = types.InlineKeyboardButton(text="Создать .txt документ анкеты", callback_data="menu2")
            button3 = types.InlineKeyboardButton(text="Поддержка", callback_data="menu3")
            button4 = types.InlineKeyboardButton(text="Назад", callback_data="Start")
            button5 = types.InlineKeyboardButton(text="Очистить все поля анкеты", callback_data="clear")
            builder.add(button1,button2,button5,button4,button3)
            builder.adjust(1)
            await message.answer(textMenu,reply_markup=builder.as_markup())

        @self.dp.message(Command("clearquestionnaire6"))
        async def clear(message: types.Message, state: FSMContext):
            await state.clear()
            await message.answer("Очистка анкеты выполнена")

        @self.dp.message(Command("questionnairemessage"))
        async def anamnes(message: types.Message, state: FSMContext):

            user_data = await state.get_data()

            if not user_data: 
                await message.answer(
                    text="Анкета не заполнена",
                )
                return 
            else:
                user_data = json.dumps(user_data, indent=4, ensure_ascii=False)

                correctKeys = Keys(user_data)
                user_data = correctKeys.changingKeys()

                await message.answer(
                text=f"<pre>{user_data}</pre>",
                parse_mode="HTML",
                reply_markup=ReplyKeyboardRemove()
                )
        
        @self.dp.message(Command("questionnairetxt"))
        async def post_txt(message:types.Document):
            file_path = "Questionnaire.txt"
            if not os.path.exists(file_path):
                await message.answer("Файл не может быть создан, так как вы не ответили ни на один вопрос в анкете.")
            else:
                document = FSInputFile(path=r'Questionnaire.txt')
                await message.bot.send_document(message.chat.id, document=document, caption="Нажмите, чтобы скачать вашу анкету")
        
        @self.dp.callback_query(F.data == 'menu2')
        async def menu2(callback_query: types.CallbackQuery):
            file_path = "Questionnaire.txt"
            if not os.path.exists(file_path):
                await callback_query.message.answer("Файл не может быть создан, так как вы не ответили ни на один вопрос в анкете.")
            else:
                document = FSInputFile(path=r'Questionnaire.txt')
                await callback_query.message.bot.send_document(callback_query.message.chat.id, document=document, caption="Нажмите, чтобы скачать вашу анкету")

        @self.dp.message(Command("help"))
        async def clear(message: types.Message):
            await message.answer("Наша поддержка https://t.me/ChocoBoy12345")

async def main():

    load_dotenv()
    dp = Dispatcher()
    r = Router()
    questionnaire = listQuestions(os.getenv('TOKEN'),dp,r)
    bot = BaseBot(os.getenv('TOKEN'), dp, questionnaire, r)

    bot.welcome()
    bot.MainMenu()
    bot.questionnaire.survey()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    aio.run(main())