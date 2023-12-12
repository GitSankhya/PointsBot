import os

import disnake
from assets import functions

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

ROLE_POINTS = {
    810625666361458699: 1,  # Tier 6
    808098501896306739: 1,  # Tier 5
    808098084562796559: 0,  # Tier 4
    802918663932870656: 0,  # Tier 3
    802918405971116042: 0,  # Tier 2
    802917803187372032: 0,  # Tier 1
    1181630576248238191: 1  # Server member
}


class AwardClient(disnake.Client):

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})\n------")

        for guild in self.guilds:
            for member in guild.members:
                for role in member.roles:
                    points = ROLE_POINTS.get(role.id)
                    if points is not None:
                        await functions.DataUpdate(None, f"INSERT INTO points(guild_id, user_id, points) VALUES(?,?,?) ON CONFLICT(guild_id, user_id) DO UPDATE SET points = points + ? WHERE guild_id = ? and user_id = ?", guild.id, member.id, points, points, guild.id, member.id)

        await self.close()

def main():
    intents = disnake.Intents.default()
    intents.members = True
    client = AwardClient(intents=intents)
    client.run(token=DISCORD_TOKEN)


if __name__ == "__main__":
    main()