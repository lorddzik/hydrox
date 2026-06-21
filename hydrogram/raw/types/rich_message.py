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


class RichMessage(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~hydrogram.raw.base.RichMessage`.

    Details:
        - Layer: ``227``
        - ID: ``BAF39D8B``

    Parameters:
        blocks (List of :obj:`PageBlock <hydrogram.raw.base.PageBlock>`):
            N/A

        photos (List of :obj:`Photo <hydrogram.raw.base.Photo>`):
            N/A

        documents (List of :obj:`Document <hydrogram.raw.base.Document>`):
            N/A

        rtl (``bool``, *optional*):
            N/A

        part (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["blocks", "photos", "documents", "rtl", "part"]

    ID = 0xbaf39d8b
    QUALNAME = "types.RichMessage"

    def __init__(self, *, blocks: List["raw.base.PageBlock"], photos: List["raw.base.Photo"], documents: List["raw.base.Document"], rtl: Optional[bool] = None, part: Optional[bool] = None) -> None:
        self.blocks = blocks  # Vector<PageBlock>
        self.photos = photos  # Vector<Photo>
        self.documents = documents  # Vector<Document>
        self.rtl = rtl  # flags.0?true
        self.part = part  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RichMessage":
        
        flags = Int.read(b)
        
        rtl = True if flags & (1 << 0) else False
        part = True if flags & (1 << 1) else False
        blocks = TLObject.read(b)
        
        photos = TLObject.read(b)
        
        documents = TLObject.read(b)
        
        return RichMessage(blocks=blocks, photos=photos, documents=documents, rtl=rtl, part=part)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rtl else 0
        flags |= (1 << 1) if self.part else 0
        b.write(Int(flags))
        
        b.write(Vector(self.blocks))
        
        b.write(Vector(self.photos))
        
        b.write(Vector(self.documents))
        
        return b.getvalue()
