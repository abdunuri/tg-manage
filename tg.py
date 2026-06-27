from telethon import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.folders import EditPeerFoldersRequest
from telethon.tl.types import InputFolderPeer
import asyncio

API_ID = 20169951
API_HASH = "19db3ec2444a2325f4a8da7faf5160a2"

client = TelegramClient("channel_manager", API_ID, API_HASH)


async def archive_chat(entity):
    try:
        await client(
            EditPeerFoldersRequest(
                folder_peers=[
                    InputFolderPeer(
                        peer=entity,
                        folder_id=1  # Archive folder
                    )
                ]
            )
        )
        return True
    except Exception as e:
        print(f"Archive failed: {e}")
        return False


async def process_channels():
    print("\n=== CHANNELS ===\n")

    async for dialog in client.iter_dialogs():
        try:
            # Broadcast channels
            if getattr(dialog.entity, "broadcast", False):
                print(f"\nChannel: {dialog.name}")
                print(f"ID: {dialog.id}")

                cmd = input(
                    "[ENTER]=Leave/Delete  | 0=Next | q=Quit : "
                ).strip().lower()

                if cmd == "q":
                    return

                if cmd == "":
                    try:
                        await client(LeaveChannelRequest(dialog.entity))
                        print("✓ Left")
                    except Exception as e:
                        print("✗ Error:", e)

        except Exception as e:
            print(e)


async def process_groups():
    print("\n=== GROUPS ===\n")

    async for dialog in client.iter_dialogs():
        try:
            # Groups and supergroups
            if dialog.is_group:
                print(f"\nGroup: {dialog.name}")
                print(f"ID: {dialog.id}")

                cmd = input(
                    "[ENTER]=Leave | a=Archive | 0=Next | q=Quit : "
                ).strip().lower()

                if cmd == "q":
                    return

                if cmd == "a":
                    await archive_chat(dialog.entity)
                    print("✓ Archived")

                elif cmd == "":
                    try:
                        await client(LeaveChannelRequest(dialog.entity))
                        print("✓ Left")
                    except Exception:
                        try:
                            await client.delete_dialog(dialog.entity)
                            print("✓ Removed")
                        except Exception as e:
                            print("✗ Error:", e)

        except Exception as e:
            print(e)


async def main():
    await client.start()

    print("\n1. Channels")
    print("2. Groups")
    print("3. Both")

    choice = input("\nChoice: ").strip()

    if choice == "1":
        await process_channels()

    elif choice == "2":
        await process_groups()

    elif choice == "3":
        await process_channels()
        await process_groups()

    print("\nDone.")


with client:
    client.loop.run_until_complete(main())