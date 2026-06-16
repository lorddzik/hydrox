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


class ToggleJoinRequest(TLObject):  # type: ignore
    """Set whether all users should request admin approval to join the group ».


    Details:
        - Layer: ``227``
        - ID: ``ECC2618``

    Parameters:
        channel (:obj:`InputChannel <hydrogram.raw.base.InputChannel>`):
            Group

        enabled (``bool``):
            Toggle

        apply_to_invites (``bool``, *optional*):
            N/A

        guard_bot (:obj:`InputUser <hydrogram.raw.base.InputUser>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "enabled", "apply_to_invites", "guard_bot"]

    ID = 0xecc2618
    QUALNAME = "functions.channels.ToggleJoinRequest"

    def __init__(self, *, channel: "raw.base.InputChannel", enabled: bool, apply_to_invites: Optional[bool] = None, guard_bot: "raw.base.InputUser" = None) -> None:
        self.channel = channel  # InputChannel
        self.enabled = enabled  # Bool
        self.apply_to_invites = apply_to_invites  # flags.1?true
        self.guard_bot = guard_bot  # flags.0?InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleJoinRequest":
        
        flags = Int.read(b)
        
        apply_to_invites = True if flags & (1 << 1) else False
        channel = TLObject.read(b)
        
        enabled = Bool.read(b)
        
        guard_bot = TLObject.read(b) if flags & (1 << 0) else None
        
        return ToggleJoinRequest(channel=channel, enabled=enabled, apply_to_invites=apply_to_invites, guard_bot=guard_bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.apply_to_invites else 0
        flags |= (1 << 0) if self.guard_bot is not None else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Bool(self.enabled))
        
        if self.guard_bot is not None:
            b.write(self.guard_bot.write())
        
        return b.getvalue()
