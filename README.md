# 📬 Gmail to Telegram Automation

Automatically reads unread emails from a specific Gmail sender and forwards their subject, body, links, and attachments to a Telegram channel — triggered on schedule using GitHub Actions.

---

## ⚙️ How It Works

1. GitHub Actions runs `main.py` every 2 hours.
2. It connects to Gmail via IMAP using secure credentials.
3. It filters unread emails from a specific sender (`test-stock@gmail.com`).
4. It parses subject, body, links, and attachments.
5. It posts the content to your Telegram channel using a bot.

---

## 🔐 Required GitHub Secrets

Add the following secrets in your repo under  
**Settings → Secrets and variables → Actions → New repository secret**:

| Name                  | Description                                      |
|-----------------------|--------------------------------------------------|
| `EMAIL_ADDRESS`       | Your Gmail address                               |
| `EMAIL_PASSWORD`      | Gmail **App Password** (see below to create one) |
| `ALLOWED_SENDER`      | Sender to filter (e.g. `test-stock@gmail.com`)   |
| `TELEGRAM_BOT_TOKEN`  | Bot token from BotFather                         |
| `TELEGRAM_CHANNEL_ID` | Your channel ID (e.g. `@your_channel`)           |

---

### 🧷 How to Create a Gmail App Password

> Required if your Gmail account has 2-Step Verification enabled.

1. Go to your Google Account → [App Passwords](https://myaccount.google.com/apppasswords)
2. Sign in and confirm 2-Step Verification is **enabled**
3. Under "Select App", choose **Mail**
4. Under "Select Device", choose **Other** → name it `GmailToTelegram`
5. Click **Generate**
6. Copy the 16-character password (no spaces) and add it to `EMAIL_PASSWORD`

⚠️ Do **not** use your regular Gmail password — it will not work.

---

## 🚀 GitHub Actions Automation

The workflow is defined in `.github/workflows/automation.yml`.

### ✅ What it does:
- Runs every 2 hours via CRON (`0 */2 * * *`)
- Sets up Python
- Installs dependencies
- Runs `main.py`

You can also trigger it manually via the **"Run workflow"** button in the Actions tab.

---

## 🧪 Install dependencies

- Run `pip install -r requirements.txt`