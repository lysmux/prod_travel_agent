from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import (
    LastPage,
    NextPage,
    CurrentPage,
    PrevPage,
    FirstPage,
    Row
)
from aiogram_dialog.widgets.text import Jinja, List, Const, Format

from bot.logic.dialogs.guide.states import GuideStates
from bot.utils.buttons import get_back_button
from .getter import data_getter

ITEMS_PER_PAGE = 2
LIST_ID = "weather_list"

window = Window(
    Jinja("guide/weather_header.html"),
    Const(" "),
    List(
        id=LIST_ID,
        field=Jinja("guide/weather_item.html"),
        items="forecasts",
        sep="\n" * 2,
        page_size=ITEMS_PER_PAGE
    ),
    Row(
        FirstPage(scroll=LIST_ID, text=Format("{target_page1}")),
        PrevPage(scroll=LIST_ID),
        CurrentPage(scroll=LIST_ID),
        NextPage(scroll=LIST_ID),
        LastPage(scroll=LIST_ID, text=Format("{target_page1}"))
    ),
    get_back_button(state=GuideStates.action),
    getter=data_getter,
    state=GuideStates.weather
)
