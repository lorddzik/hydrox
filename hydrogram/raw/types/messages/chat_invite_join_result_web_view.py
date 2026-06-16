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


class ChatInviteJoinResultWebView(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~hydrogram.raw.base.messages.ChatInviteJoinResult`.

    Details:
        - Layer: ``227``
        - ID: ``2F51C337``

    Parameters:
        bot_id (``int`` ``64-bit``):
            N/A

        webview (:obj:`WebViewResult <hydrogram.raw.base.WebViewResult>`):
            N/A

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ImportChatInvite
            channels.JoinChannel
    """

    __slots__: List[str] = ["bot_id", "webview", "users"]

    ID = 0x2f51c337
    QUALNAME = "types.messages.ChatInviteJoinResultWebView"

    def __init__(self, *, bot_id: int, webview: "raw.base.WebViewResult", users: List["raw.base.User"]) -> None:
        self.bot_id = bot_id  # long
        self.webview = webview  # WebViewResult
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInviteJoinResultWebView":
        # No flags
        
        bot_id = Long.read(b)
        
        webview = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ChatInviteJoinResultWebView(bot_id=bot_id, webview=webview, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.bot_id))
        
        b.write(self.webview.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()
