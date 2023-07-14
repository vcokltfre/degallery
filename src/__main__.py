from asyncio import run
from os import environ

from disnake import CommandInteraction, Message
from disnake.ext.commands import InteractionBot
from dotenv import load_dotenv


load_dotenv()


async def main() -> None:
    bot = InteractionBot()

    @bot.message_command(name="degallery")  # type: ignore
    async def degallery(itr: CommandInteraction, message: Message):  # type: ignore
        urls: list[str] = []

        for attachment in message.attachments:
            url = attachment.url

            if url.endswith((".png", ".jpg", ".jpeg", ".gif")):
                urls.append(url)

        if urls:
            await itr.response.send_message("\n".join(urls))

    @bot.listen()
    async def on_ready() -> None:  # type: ignore
        print("Ready!")

    await bot.start(environ["TOKEN"])


if __name__ == "__main__":
    run(main())
