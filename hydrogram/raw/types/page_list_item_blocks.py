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


class PageListItemBlocks(TLObject):  # type: ignore
    """List item

    Constructor of :obj:`~hydrogram.raw.base.PageListItem`.

    Details:
        - Layer: ``227``
        - ID: ``63CA67AA``

    Parameters:
        blocks (List of :obj:`PageBlock <hydrogram.raw.base.PageBlock>`):
            Blocks

        checkbox (``bool``, *optional*):
            N/A

        checked (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["blocks", "checkbox", "checked"]

    ID = 0x63ca67aa
    QUALNAME = "types.PageListItemBlocks"

    def __init__(self, *, blocks: List["raw.base.PageBlock"], checkbox: Optional[bool] = None, checked: Optional[bool] = None) -> None:
        self.blocks = blocks  # Vector<PageBlock>
        self.checkbox = checkbox  # flags.0?true
        self.checked = checked  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageListItemBlocks":
        
        flags = Int.read(b)
        
        checkbox = True if flags & (1 << 0) else False
        checked = True if flags & (1 << 1) else False
        blocks = TLObject.read(b)
        
        return PageListItemBlocks(blocks=blocks, checkbox=checkbox, checked=checked)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.checkbox else 0
        flags |= (1 << 1) if self.checked else 0
        b.write(Int(flags))
        
        b.write(Vector(self.blocks))
        
        return b.getvalue()
