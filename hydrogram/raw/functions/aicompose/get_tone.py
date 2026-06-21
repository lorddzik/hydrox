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


class GetTone(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``B2E8BA03``

    Parameters:
        tone (:obj:`InputAiComposeTone <hydrogram.raw.base.InputAiComposeTone>`):
            N/A

    Returns:
        :obj:`aicompose.Tones <hydrogram.raw.base.aicompose.Tones>`
    """

    __slots__: List[str] = ["tone"]

    ID = 0xb2e8ba03
    QUALNAME = "functions.aicompose.GetTone"

    def __init__(self, *, tone: "raw.base.InputAiComposeTone") -> None:
        self.tone = tone  # InputAiComposeTone

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTone":
        # No flags
        
        tone = TLObject.read(b)
        
        return GetTone(tone=tone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.tone.write())
        
        return b.getvalue()
