#  Hydrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2023 Dan <https://github.com/delivrance>
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

from __future__ import annotations

from typing import TYPE_CHECKING

import hydrogram
from hydrogram import raw, utils
from hydrogram.types.object import Object

if TYPE_CHECKING:
    from datetime import datetime


class EmojiStatus(Object):
    """A user emoji status.

    Parameters:
        custom_emoji_id (``int``):
            Custom emoji id.

        until_date (:py:obj:`~datetime.datetime`, *optional*):
            Valid until date.
    """

    def __init__(
        self,
        *,
        client: hydrogram.Client = None,
        custom_emoji_id: int,
        until_date: datetime | None = None,
    ):
        super().__init__(client)

        self.custom_emoji_id = custom_emoji_id
        self.until_date = until_date

    @staticmethod
    def _parse(client, emoji_status: raw.base.EmojiStatus) -> EmojiStatus | None:
        if isinstance(emoji_status, raw.types.EmojiStatus):
            until_date = None
            if getattr(emoji_status, "until", None) is not None:
                until_date = utils.timestamp_to_datetime(emoji_status.until)
            return EmojiStatus(
                client=client,
                custom_emoji_id=emoji_status.document_id,
                until_date=until_date,
            )

        collectible_cls = getattr(raw.types, "EmojiStatusCollectible", None)
        if collectible_cls and isinstance(emoji_status, collectible_cls):
            until_date = None
            if getattr(emoji_status, "until", None) is not None:
                until_date = utils.timestamp_to_datetime(emoji_status.until)
            return EmojiStatus(
                client=client,
                custom_emoji_id=emoji_status.document_id,
                until_date=until_date,
            )

        return None

    def write(self):
        until = utils.datetime_to_timestamp(self.until_date) if self.until_date else None
        return raw.types.EmojiStatus(
            document_id=self.custom_emoji_id,
            until=until,
        )
