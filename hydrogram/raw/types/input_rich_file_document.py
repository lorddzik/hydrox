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


class InputRichFileDocument(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~hydrogram.raw.base.InputRichFile`.

    Details:
        - Layer: ``227``
        - ID: ``83281DBD``

    Parameters:
        id (``str``):
            N/A

        document (:obj:`InputDocument <hydrogram.raw.base.InputDocument>`):
            N/A

    """

    __slots__: List[str] = ["id", "document"]

    ID = 0x83281dbd
    QUALNAME = "types.InputRichFileDocument"

    def __init__(self, *, id: str, document: "raw.base.InputDocument") -> None:
        self.id = id  # string
        self.document = document  # InputDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputRichFileDocument":
        # No flags
        
        id = String.read(b)
        
        document = TLObject.read(b)
        
        return InputRichFileDocument(id=id, document=document)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.id))
        
        b.write(self.document.write())
        
        return b.getvalue()
