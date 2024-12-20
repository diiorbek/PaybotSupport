from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


lang_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek", callback_data="lang_uz"),
        ],
				[
						InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
				]
    ],
)

category_button_uz = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="👀 1-kategoriya", callback_data="category_1")
		],
		[
			InlineKeyboardButton(text="🎉 2-kategoriya", callback_data="category_2")
		],
		[
			InlineKeyboardButton(text="✨ 3-kategoriya", callback_data="category_3")
		],
		[
			InlineKeyboardButton(text="🎁 4-kategoriya", callback_data="category_4")
		],
		[
			InlineKeyboardButton(text="🙌 5-kategoriya", callback_data="category_5")
		],
	]
)

category_button_ru = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="👀 1-категория", callback_data="category_1")
		],
		[
			InlineKeyboardButton(text="🎉 2-категория", callback_data="category_2")
		],
		[
			InlineKeyboardButton(text="✨ 3-категория", callback_data="category_3")
		],
		[
			InlineKeyboardButton(text="🎁 4-категория", callback_data="category_4")
		],
		[
			InlineKeyboardButton(text="🙌 5-категория", callback_data="category_5")
		],
	]
)

question_button_uz = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="👀 1-savol", callback_data="question_1")
		],
		[
			InlineKeyboardButton(text="🎉 2-savol", callback_data="question_2")
		],
		[
			InlineKeyboardButton(text="✨ 3-savol", callback_data="question_3")
		],
		[
			InlineKeyboardButton(text="🎁 4-savol", callback_data="question_4")
		],
		[
			InlineKeyboardButton(text="🙌 5-savol", callback_data="question_5")
		],
		[
			InlineKeyboardButton(text="⬅️ Asosiy menyu", callback_data="menu")
		]
	]
)

question_button_ru = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="👀 1-вопрос", callback_data="question_1")
		],
		[
			InlineKeyboardButton(text="🎉 2-вопрос", callback_data="question_2")
		],
		[
			InlineKeyboardButton(text="✨ 3-вопрос", callback_data="question_3")
		],
		[
			InlineKeyboardButton(text="🎁 4-вопрос", callback_data="question_4")
		],
		[
			InlineKeyboardButton(text="🙌 5-вопрос", callback_data="question_5")
		],
		[
			InlineKeyboardButton(text="⬅️ Главное меню", callback_data="menu")
		]
	]
)

menu_button_uz = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="⬅️ Asosiy menyu", callback_data="menu")
		]
	]	
)

menu_button_ru = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="⬅️ Главное меню", callback_data="menu")
		]
	]	
)

answer_button = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="✨ Javob berish", callback_data="admin_answer")
		]
	]
)