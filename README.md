# 📧 Excel to Email Automation

This Python project automates sending emails using **Gmail** credentials via **"Sign in with App Passwords"**. The script reads recipient details from an **Excel sheet** and sends personalized emails automatically.

---

## 🚀 Features
✅ Reads recipient data (Name, Email, Subject, Message) from an **Excel file**  
✅ Sends **personalized emails** using a predefined **HTML template**  
✅ Uses **Gmail SMTP** authentication with **App Passwords** for security  
✅ Logs email activity and errors for debugging  
✅ Supports **batch email sending** to prevent spam detection  

---

## 📂 Project Structure
```
ExcelPost/
│── data/                      # Storage for Excel files
│   ├── contacts.xlsx          # Excel file containing email data
│── logs/                      # Log files for tracking emails
│   ├── email_log.txt          # Sent email history
│   ├── error_log.txt          # Error tracking
│── templates/                 # Email templates
│   ├── template.html          # HTML email template
│── src/                       # Python source code
│   ├── mailer.py              # Handles email sending
│   ├── excel_reader.py        # Reads & processes Excel data
│   ├── main.py                # Main script to execute automation
│── .env                       # Environment variables
│── README.md                  # Documentation
│── requirements.txt           # Python dependencies
```

---

## 🛠️ Setup Instructions

### 1️⃣ **Install Dependencies**
Ensure you have **Python 3.x** installed, then install required libraries:
```sh
pip install -r requirements.txt
```

---

### 2️⃣ **Enable "App Passwords" in Gmail**
Since Google **blocks less secure apps**, you must use an **App Password** instead of your normal password.

#### 🔹 Steps to Generate an App Password:
1. Go to **[Google Account Security](https://myaccount.google.com/security)**  
2. Under **"Signing in to Google"**, select **"App Passwords"**  
3. Choose **"Mail"** as the app and **"Other (Custom name)"** (e.g., "ExcelPost")  
4. Copy the **16-character password** and **save it securely**  

---

---

### 4️⃣ **Prepare Your Excel File**
Edit `data/contacts.xlsx` to include the following columns:
| Name          | Email                  | Subject                  | Message                                   |
|--------------|------------------------|--------------------------|-------------------------------------------|
| John Doe     | johndoe@example.com     | Welcome to Our Service!  | Hi John, welcome to our platform!        |
| Jane Smith   | janesmith@example.com   | Subscription Update      | Your subscription has been renewed.      |

---

### 5️⃣ **Run the Script**
Execute the automation:
```sh
python src/main.py
```
📧 Emails will be sent to recipients listed in `contacts.xlsx`!

---

## 📜 License
This project is open-source and available under the **MIT License**.  
