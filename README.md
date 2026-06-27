# Telegram Channel & Group Manager

A simple Python script built with Telethon that helps you manually review and manage your Telegram channels and groups one by one.

## Features

### Channels

* Iterates through all channels in your account.
* Displays each channel individually.
* Available actions:

  * **Press Enter** → Leave/Delete the channel.
  * **Type `0`** → Skip to the next channel.
  * **Type `q`** → Quit the process.

### Groups

* Iterates through all groups and supergroups.
* Displays each group individually.
* Available actions:

  * **Press Enter** → Leave the group.
  * **Type `a`** → Archive the group.
  * **Type `0`** → Skip to the next group.
  * **Type `q`** → Quit the process.

---

## Requirements

* Python 3.8+
* Telethon

Install dependencies:

```bash
pip install telethon
```

---

## Getting Telegram API Credentials

This script uses Telegram's official API through Telethon.

To obtain your credentials:

1. Visit https://my.telegram.org/apps
2. Log in using your Telegram account.
3. Create a new application.
4. Copy your:

   * **API ID**
   * **API HASH**

These credentials are tied to your Telegram account and are required to access Telegram through the API.

---

## Configuration

You can provide your API credentials in two ways.

### Option 1: Enter at runtime

```python
API_ID = int(input("API ID: "))
API_HASH = input("API HASH: ")
```

This method is recommended if you do not want to store credentials inside the source code.

### Option 2: Save as constants

```python
API_ID = 12345678
API_HASH = "your_api_hash_here"
```

If using this approach, remove or comment out the input statements.

---

## Running the Script

Run:

```bash
python main.py
```

On the first run, Telethon will ask for:

* Your phone number
* The login verification code sent by Telegram
* Your 2FA password (if enabled)

A session file named:

```
channel_manager.session
```

will be created. Future runs will use this session, so you won't need to log in again.

---

## Menu

After login, choose what to process:

```
1. Channels
2. Groups
3. Both
```

---

## Channel Controls

```
[ENTER] = Leave/Delete channel
0       = Skip channel
q       = Quit
```

Example:

```
Channel: Example News
ID: 123456789

[ENTER]=Leave/Delete | 0=Next | q=Quit:
```

---

## Group Controls

```
[ENTER] = Leave group
a       = Archive group
0       = Skip group
q       = Quit
```

Example:

```
Group: Friends Group
ID: 987654321

[ENTER]=Leave | a=Archive | 0=Next | q=Quit:
```

---

## Notes

* This script performs actions immediately; there is no confirmation prompt.
* Archiving moves a chat to Telegram's archived folder.
* Leaving channels and groups cannot be automatically undone.
* Always review the displayed chat name carefully before pressing Enter.

---

## Disclaimer

This tool uses Telegram's official API via Telethon and operates only on your own Telegram account. Use it responsibly and ensure you understand the action before leaving or archiving chats.
