#  Hydrogram - Telegram MTProto API Client Library for Python
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

from io import BytesIO

from hydrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hydrogram.raw.core import TLObject
from hydrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class InputBotInlineMessageRichMessage(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~hydrogram.raw.base.InputBotInlineMessage`.

    Details:
        - Layer: ``227``
        - ID: ``B43DF56C``

    Parameters:
        rich_message (:obj:`InputRichMessage <hydrogram.raw.base.InputRichMessage>`):
            N/A

        reply_markup (:obj:`ReplyMarkup <hydrogram.raw.base.ReplyMarkup>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["rich_message", "reply_markup"]

    ID = 0xb43df56c
    QUALNAME = "types.InputBotInlineMessageRichMessage"

    def __init__(self, *, rich_message: "raw.base.InputRichMessage", reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.rich_message = rich_message  # InputRichMessage
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineMessageRichMessage":
        
        flags = Int.read(b)
        
        reply_markup = TLObject.read(b) if flags & (1 << 2) else None
        
        rich_message = TLObject.read(b)
        
        return InputBotInlineMessageRichMessage(rich_message=rich_message, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        b.write(Int(flags))
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        b.write(self.rich_message.write())
        
        return b.getvalue()
