# 📧 System Automation — Browser-Based Email Sender

Automates the process of sending a simple email entirely through the browser — no SMTP or email library required. Built with **Python**, **Selenium** (browser control) and **PyAutoGUI** (mouse & keyboard simulation).

---

## 🚀 How It Works

The script launches a Chrome browser, navigates to your email provider's web interface, logs in, and uses UI automation to compose and send an email — simulating real human interactions like clicking, typing and pressing keyboard shortcuts.

```
[Script starts]
     ↓
[Opens Chrome via Selenium]
     ↓
[Navigates to email provider login page]
     ↓
[Types credentials with PyAutoGUI / Selenium]
     ↓
[Composes email (recipient, subject, body)]
     ↓
[Sends email]
```

---

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8+
- Google Chrome installed
- [ChromeDriver](https://chromedriver.chromium.org/downloads) matching your Chrome version

### 1. Clone the repository

```bash
git clone https://github.com/henrique-svg21/System_Automation.git
cd System_Automation
```

### 2. Install dependencies

```bash
pip install selenium pyautogui python-dotenv
```

> 💡 **Tip:** Use a virtual environment to keep things organized.
> ```bash
> python -m venv venv
> source venv/bin/activate      # Linux/macOS
> venv\Scripts\activate         # Windows
> pip install selenium pyautogui python-dotenv
> ```

### 3. Set up ChromeDriver

Download ChromeDriver for your Chrome version and either:
- Place the `chromedriver` executable in the project root, **or**
- Add it to your system `PATH`

> To check your Chrome version: go to `chrome://settings/help` in your browser.

---

## 🔐 Configuration

Credentials are stored in a `.env` file to keep them out of version control.

### 1. Create a `.env` file in the project root

```env
EMAIL=your_email@gmail.com
PASSWORD=your_password
```

### 2. Make sure `.env` is listed in `.gitignore`

```
# .gitignore
.env
```

> ⚠️ **Never commit your `.env` file to GitHub.** Your credentials will be exposed publicly.

### 3. Load the credentials in your script

```python
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL     = os.getenv("EMAIL")
PASSWORD  = os.getenv("PASSWORD")
```

---

## ▶️ Usage

Run the main script:

```bash
python main.py
```

The script will automatically:
1. Open Google Chrome
2. Navigate to the email provider's login page
3. Log in with your credentials from `.env`
4. Open the compose window
5. Fill in the recipient, subject, and body
6. Send the email

### Example automation snippet

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui, time

driver = webdriver.Chrome()
driver.get("https://mail.google.com")

# Log in
driver.find_element(By.ID, "identifierId").send_keys(EMAIL)
# ... continue login steps ...

# Compose & send
pyautogui.hotkey("ctrl", "shift", "c")     # Open compose window
time.sleep(1)
pyautogui.write(RECIPIENT, interval=0.05)  # Type recipient
pyautogui.hotkey("ctrl", "enter")          # Send
```

---

## ⚠️ Important Notes

- Keep the **browser window visible and in focus** while the script runs — PyAutoGUI controls the mouse and keyboard at screen level.
- Make sure your **screen resolution and browser zoom** are consistent across runs, as PyAutoGUI relies on coordinates.
- Some email providers may block automated logins. You may need to enable **"Less secure app access"** or use an **App Password** (recommended for Gmail personal accounts).

---

## 📁 Project Structure

```
System_Automation/
├── main.py        # Main automation script
├── .env           # Credentials (not committed)
├── .gitignore ]    # Ignores .env and other local files
└── Email.py       #contains receiver's email, title and body message (optional, can be done directly in the code)
└── README.md
```

---

## 📄 License

Copyright (c) 2026 Henrique Schorck

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

#