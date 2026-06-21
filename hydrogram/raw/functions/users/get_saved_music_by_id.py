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


class GetSavedMusicByID(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``7573A4E9``

    Parameters:
        id (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            N/A

        documents (List of :obj:`InputDocument <hydrogram.raw.base.InputDocument>`):
            N/A

    Returns:
        :obj:`users.SavedMusic <hydrogram.raw.base.users.SavedMusic>`
    """

    __slots__: List[str] = ["id", "documents"]

    ID = 0x7573a4e9
    QUALNAME = "functions.users.GetSavedMusicByID"

    def __init__(self, *, id: "raw.base.InputUser", documents: List["raw.base.InputDocument"]) -> None:
        self.id = id  # InputUser
        self.documents = documents  # Vector<InputDocument>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSavedMusicByID":
        # No flags
        
        id = TLObject.read(b)
        
        documents = TLObject.read(b)
        
        return GetSavedMusicByID(id=id, documents=documents)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        b.write(Vector(self.documents))
        
        return b.getvalue()
