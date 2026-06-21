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


class Tones(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~hydrogram.raw.base.aicompose.Tones`.

    Details:
        - Layer: ``227``
        - ID: ``6C9D0EFE``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        tones (List of :obj:`AiComposeTone <hydrogram.raw.base.AiComposeTone>`):
            N/A

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            aicompose.GetTone
            aicompose.GetTones
    """

    __slots__: List[str] = ["hash", "tones", "users"]

    ID = 0x6c9d0efe
    QUALNAME = "types.aicompose.Tones"

    def __init__(self, *, hash: int, tones: List["raw.base.AiComposeTone"], users: List["raw.base.User"]) -> None:
        self.hash = hash  # long
        self.tones = tones  # Vector<AiComposeTone>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Tones":
        # No flags
        
        hash = Long.read(b)
        
        tones = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return Tones(hash=hash, tones=tones, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.tones))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
