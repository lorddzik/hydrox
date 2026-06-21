#  Hydrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2023 Dan <https://github.com/delivrance>
#  Copyright (C) 2023-present Hydrogram <https://hydrogram.org>
#
#  This file is part of Hydrogram.
#
#  Hydrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Hydrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Hydrogram.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

from typing import Any

from hydrogram import raw, types
from hydrogram.types.object import Object


class KeyboardButton(Object):
    """One button of the reply keyboard.
    For simple text buttons String can be used instead of this object to specify text of the button.
    Optional fields are mutually exclusive.

    Parameters:
        text (``str``):
            Text of the button. If none of the optional fields are used, it will be sent as a message when
            the button is pressed.

        request_contact (``bool``, *optional*):
            If True, the user's phone number will be sent as a contact when the button is pressed.
            Available in private chats only.

        request_location (``bool``, *optional*):
            If True, the user's current location will be sent when the button is pressed.
            Available in private chats only.

        web_app (:obj:`~hydrogram.types.WebAppInfo`, *optional*):
            If specified, the described `Web App <https://core.telegram.org/bots/webapps>`_ will be launched when the
            button is pressed. The Web App will be able to send a “web_app_data” service message. Available in private
            chats only.

    """

    def __init__(
        self,
        text: str | Any,
        request_contact: bool | None = None,
        request_location: bool | None = None,
        web_app: types.WebAppInfo = None,
        style: str | None = None,
        icon_custom_emoji_id: str | int | None = None,
    ):
        super().__init__()

        self.text = text if isinstance(text, str) else str(text)
        self.request_contact = request_contact
        self.request_location = request_location
        self.web_app = web_app
        self.style = style
        self.icon_custom_emoji_id = icon_custom_emoji_id

    @staticmethod
    def read(b):
        if isinstance(b, raw.types.KeyboardButton):
            return b.text

        if isinstance(b, raw.types.KeyboardButtonRequestPhone):
            return KeyboardButton(text=b.text, request_contact=True)

        if isinstance(b, raw.types.KeyboardButtonRequestGeoLocation):
            return KeyboardButton(text=b.text, request_location=True)

        if isinstance(b, raw.types.KeyboardButtonSimpleWebView):
            return KeyboardButton(text=b.text, web_app=types.WebAppInfo(url=b.url))
        return None

    def write(self):
        style_obj = None
        if self.style is not None or self.icon_custom_emoji_id is not None:
            bg_primary = self.style == "primary"
            bg_danger = self.style == "danger"
            bg_success = self.style == "success"
            icon = int(self.icon_custom_emoji_id) if self.icon_custom_emoji_id is not None else None
            style_obj = raw.types.KeyboardButtonStyle(
                bg_primary=bg_primary,
                bg_danger=bg_danger,
                bg_success=bg_success,
                icon=icon
            )

        if self.request_contact:
            return raw.types.KeyboardButtonRequestPhone(text=self.text, style=style_obj)
        if self.request_location:
            return raw.types.KeyboardButtonRequestGeoLocation(text=self.text, style=style_obj)
        if self.web_app:
            return raw.types.KeyboardButtonSimpleWebView(text=self.text, url=self.web_app.url, style=style_obj)
        return raw.types.KeyboardButton(text=self.text, style=style_obj)
