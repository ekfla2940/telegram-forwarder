from telethon import TelegramClient, events

api_id = 34354743
api_hash = "56aae39aabd214ef8b7d97a077fd138a"

source_chat = -4220344471
target_chat = -4216190775

keywords = ["raw material", "#", "ready"]

client = TelegramClient("session", api_id, api_hash)

def check(text):
    if not text:
        return False
    text = text.lower()
    return any(k in text for k in keywords)

@client.on(events.NewMessage(chats=source_chat))
async def handler(event):
    msg = event.message.message or ""

    if check(msg):
        try:
            await client.forward_messages(target_chat, event.message)
            print("포워드됨:", msg)
        except Exception as e:
            print("에러:", e)

async def main():
    me = await client.get_me()
    print("로그인됨:", me.first_name)
    print("실행중...")

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()