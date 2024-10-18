from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Оценить уровень артериального давления'),
         KeyboardButton(text='О нас')]
    ],
    resize_keyboard=True
)

cont_ill_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
                     [InlineKeyboardButton(text="Сахарный диабет", callback_data="diabetes")],
                     [InlineKeyboardButton(text="Ишемическая болезнь сердца", callback_data="CHD")],
                     [InlineKeyboardButton(text="Инсульт", callback_data="insult")],
                     [InlineKeyboardButton(text="Хроническая болезнь почек", callback_data="CKD")],
                     [InlineKeyboardButton(text="Нет сопутсвующих заболеваний", callback_data="nothing")],
                     [InlineKeyboardButton(text="Готово", callback_data="done")]
    ])

SMD = InlineKeyboardMarkup(
    inline_keyboard=[
                    [InlineKeyboardButton(text='Да', callback_data='yes')],
                    [InlineKeyboardButton(text='Нет', callback_data='no')]
    ]
)


about_btn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='наша группа в вк',
                                                                        url='https://vk.ru/nebolej74')]])
symptom_key = InlineKeyboardMarkup(
    inline_keyboard=[
                    [InlineKeyboardButton(text='Да', callback_data='yes_s'),
                    InlineKeyboardButton(text='Нет', callback_data='no_s')]])

has_ag_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='Да', callback_data='Yes_ag'), InlineKeyboardButton(text='Нет', callback_data='No_ag')]]
)
