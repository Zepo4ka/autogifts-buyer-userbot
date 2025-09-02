from typing import List

import pyrogram
from pyrogram import raw, types


class GetAvailableGifts:
    async def get_available_gifts(
        self: "pyrogram.Client",
    ) -> List["types.Gift"]:

        r = await self.invoke(
            raw.functions.payments.GetStarGifts(hash=0)
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}
        return r.gifts
