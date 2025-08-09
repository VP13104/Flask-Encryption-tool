# 🔐 AES-256-CBC Encryption & Decryption Web Tool

A simple yet secure **web-based encryption and decryption tool** built with **Flask** for the backend and **HTML/CSS/JavaScript** for the frontend.  
This tool allows you to encrypt and decrypt both text and files using the **AES-256-CBC** algorithm.

---

## 📌 Features
- **AES-256-CBC Encryption & Decryption** for high security.
- Encrypt or decrypt **text** or **files**.
- Option to enter a **custom 32-character key**.
- Automatic IV (Initialization Vector) handling for files.
- Clean UI with separate **Encrypt** and **Decrypt** pages.
- Fully implemented in **Flask + Python (cryptography)**.

---

## 🛠 Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Encryption Library**: `cryptography`

---

## 📂 Project Structure
│<br>
├── app.py # Main Flask backend <br>
├── encryption_crypto_utils.py # Encryption/Decryption logic<br>
├── requirements.txt # Python dependencies<br>
├── README.md # Project documentation<br>
│<br>
├── templates/ # HTML files<br>
│ ├── main.html<br>
│ ├── encrypt.html<br>
│ ├── decrypt.html<br>
│<br>
├── static/ # Static assets<br>
│ ├── decrypt.jpg<br>
| ├── encrypt.jpg<br>
│ ├── file3.jpeg # Image used in UI<br>
| ├── hover.js # JS for hover effect<br>
| ├── style.css #stylesheet <br>
| ├── stylee.css #stylesheet <br>
│<br>

---


## ⚙️ Installation & Usage

### 1️⃣ Clone the Repository
git clone https://github.com/VP13104/Flask-Encryption-tool.git <br>
cd Flask-Encryption-tool

### 2️⃣ Install Dependencies
pip install -r requirments.txt

### 3️⃣ Run the Application
python app.py
