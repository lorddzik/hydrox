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


class GetPollResults(TLObject):  # type: ignore
    """Get poll results


    Details:
        - Layer: ``227``
        - ID: ``EDA3E33B``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Peer where the poll was found

        msg_id (``int`` ``32-bit``):
            Message ID of poll message

        poll_hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "msg_id", "poll_hash"]

    ID = 0xeda3e33b
    QUALNAME = "functions.messages.GetPollResults"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, poll_hash: int) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.poll_hash = poll_hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPollResults":
        # No flags
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        poll_hash = Long.read(b)
        
        return GetPollResults(peer=peer, msg_id=msg_id, poll_hash=poll_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Long(self.poll_hash))
        
        return b.getvalue()
