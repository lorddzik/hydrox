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


class SendBotRequestedPeer(TLObject):  # type: ignore
    """Send one or more chosen peers, as requested by a keyboardButtonRequestPeer button.


    Details:
        - Layer: ``227``
        - ID: ``6C5CF2A7``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            The bot that sent the keyboardButtonRequestPeer button.

        button_id (``int`` ``32-bit``):
            The button_id field from the keyboardButtonRequestPeer constructor.

        requested_peers (List of :obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            The chosen peers.

        msg_id (``int`` ``32-bit``, *optional*):
            ID of the message that contained the reply keyboard with the keyboardButtonRequestPeer button.

        webapp_req_id (``str``, *optional*):
            N/A

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "button_id", "requested_peers", "msg_id", "webapp_req_id"]

    ID = 0x6c5cf2a7
    QUALNAME = "functions.messages.SendBotRequestedPeer"

    def __init__(self, *, peer: "raw.base.InputPeer", button_id: int, requested_peers: List["raw.base.InputPeer"], msg_id: Optional[int] = None, webapp_req_id: Optional[str] = None) -> None:
        self.peer = peer  # InputPeer
        self.button_id = button_id  # int
        self.requested_peers = requested_peers  # Vector<InputPeer>
        self.msg_id = msg_id  # flags.0?int
        self.webapp_req_id = webapp_req_id  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendBotRequestedPeer":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b) if flags & (1 << 0) else None
        webapp_req_id = String.read(b) if flags & (1 << 1) else None
        button_id = Int.read(b)
        
        requested_peers = TLObject.read(b)
        
        return SendBotRequestedPeer(peer=peer, button_id=button_id, requested_peers=requested_peers, msg_id=msg_id, webapp_req_id=webapp_req_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.msg_id is not None else 0
        flags |= (1 << 1) if self.webapp_req_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.msg_id is not None:
            b.write(Int(self.msg_id))
        
        if self.webapp_req_id is not None:
            b.write(String(self.webapp_req_id))
        
        b.write(Int(self.button_id))
        
        b.write(Vector(self.requested_peers))
        
        return b.getvalue()
