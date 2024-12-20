from aiogram.types import Message, CallbackQuery
from loader import dp,db,bot,GROUPS
from aiogram.filters import CommandStart
from keyboard_buttons import user_keyboard
from aiogram import F
from states.states import AdminMessage
from aiogram.fsm.context import FSMContext

questions = dict()


@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text="""Пожалуйста, выберите язык общения.

Muloqot tilini tanglang.""", reply_markup=user_keyboard.lang_button)
    except:
        await message.answer(text="""Пожалуйста, выберите язык общения.

Muloqot tilini tanglang.""", reply_markup=user_keyboard.lang_button)

@dp.callback_query(F.data.startswith('lang'))
async def choice_language(callback: CallbackQuery):
    await callback.message.delete()
    try:
        user_lang = callback.data.split('_')[1]
        db.add_user(full_name=callback.from_user.full_name, telegram_id=callback.from_user.id, language=user_lang)
        if user_lang == "uz":
            await callback.message.answer(text="""Iltimos, savolingiz nima bilan bog'liqligini ayting.

Quyidagi menyudan tanlang""", reply_markup=user_keyboard.category_button_uz)
            
        elif user_lang == "ru":
            await callback.message.answer(text="""Пожалуйста, скажите с чем связан ваш вопрос.

Выберите из этого меню.""", reply_markup=user_keyboard.category_button_ru)
    
    except:
        
        db.update_language(telegram_id=callback.from_user.id, new_language=user_lang)
        if user_lang == "uz":
            await callback.message.answer(text="""Iltimos, savolingiz nima bilan bog'liqligini ayting.

Quyidagi menyudan tanlang""", reply_markup=user_keyboard.category_button_uz)
            
        elif user_lang == "ru":
            await callback.message.answer(text="""Пожалуйста, скажите с чем связан ваш вопрос.

Выберите из этого меню.""", reply_markup=user_keyboard.category_button_ru)
            

@dp.callback_query(F.data.startswith('category'))
async def category_request(callback: CallbackQuery):
    user_lang = db.get_language(telegram_id=callback.from_user.id)

    if user_lang == "uz":
        user_category = callback.data.split('_')[1]
        await callback.message.edit_text(text=f"{user_category} bo'yicha savollar.", reply_markup=user_keyboard.question_button_uz)

    elif user_lang == "ru":
        user_category = callback.data.split('_')[1]
        await callback.message.edit_text(text=f"Вопросы по {user_category} категории.", reply_markup=user_keyboard.question_button_ru)

@dp.callback_query(F.data.startswith('question'))
async def question_request(callback: CallbackQuery):
    user_lang = db.get_language(telegram_id=callback.from_user.id)

    user_question = callback.data.split('_')[1]
    if user_lang == "uz":
        await callback.message.edit_text(text=f"{user_question} savolga javob.", reply_markup=user_keyboard.menu_button_uz)

    if user_lang == "ru":
        await callback.message.edit_text(text=f"Ответ для {user_question} вопроса.", reply_markup=user_keyboard.menu_button_ru)

@dp.callback_query(F.data == "menu")
async def menu_request(callback: CallbackQuery):
    user_lang = db.get_language(telegram_id=callback.from_user.id)


    if user_lang == "uz":
        await callback.message.edit_text(text="""Iltimos, savolingiz nima bilan bog'liqligini ayting.

Quyidagi menyudan tanlang""", reply_markup=user_keyboard.category_button_uz)
            
    elif user_lang == "ru":
        await callback.message.edit_text(text="""Пожалуйста, скажите с чем связан ваш вопрос.

Выберите из этого меню.""", reply_markup=user_keyboard.category_button_ru)

    await callback.message.answer(text="Savolingizga javob topmadingizmi? Unda savolingizni yozib qoldiring.")

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@dp.message(F.text)
async def send_to_group_text(message: Message):
    questions[message.from_user.id] = message.text
    answer_button = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="✨ Javob berish", callback_data=f"admin_answer_{message.from_user.id}")
		]
	]
)
    await bot.send_message(chat_id=GROUPS[0], text=f"Savol raqami: <b>#52</b>\n\nFoydalanuvchi: <b>{message.from_user.full_name}</b>\nSavol: <b>{message.text}</b>", reply_markup=user_keyboard.answer_button)
    await message.answer(text="Savolingiz adminga yuborildi va tez orada ko'rib chiqiladi.\nAfar savolingizga 1 soat ichida javob olmasangiz, chat avtomatik tarzda yopiladi va siz bilan qayta bog'lanish kerak bo'ladi!")

@dp.callback_query(F.data.startswith("admin_answer"))
async def send_admin_answer_to_user(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.set_state(AdminMessage.text)
    await bot.send_message(chat_id=callback.from_user.id, text="Javobni yozishingiz mumkin!")
    