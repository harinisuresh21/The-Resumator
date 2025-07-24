# 🧠 The Résumator 🔥  
“Hasta la vista, messy resumes.”  

A smart and stylish resume parser web application built with **Python (Flask)**, **spaCy**, and a modern frontend. Just upload a PDF or DOCX resume and instantly extract key details like **name**, **email**, **skills**, and **experience**!

---

## 🚀 Features

- 🔍 Extracts candidate information using NLP:
  - Name (even if not labeled)
  - Email
  - Phone number
  - Skills (required + matched)
  - Experience / Internship blocks

- 🧑‍💻 Upload-friendly UI with animations
- 🎨 Responsive & aesthetic frontend
- ✅ Supports `.pdf` and `.docx` formats
- ⚙️ Deployed on Render (or your preferred hosting)

---

## 📸 Demo

| Upload Page | Result Page |
|-------------|-------------|
| ![Upload](screenshots/upload.png) | ![Result](screenshots/result.png) |

---

## 🛠️ Tech Stack

**Frontend**:  
- HTML5, CSS3, JavaScript  
- Google Fonts + Flexbox Layout  
- Responsive Design + Animations

**Backend**:  
- Python (Flask)  
- NLP using spaCy  
- Regex for email, phone, and experience  
- File handling for PDF & DOCX

---

<pre>  📂 Project Structure
resume-parser/
│
├── app.py # Flask application logic
├── requirements.txt # Python dependencies
│
├── templates/
│ ├── index.html # Homepage (upload UI)
│ └── result.html # Display parsed result
│
├── static/
│ ├── style.css # Styles for index page
│ └── result.css # Styles for result page
│
└── README.md </pre>



---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/harinisuresh21/The-Resumator.git
cd The-Resumator
```
### 2. Create and Activate Virtual Environment
```
python -m venv venv
# Activate it:
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Run the Flask App
```
   python app.py 
   ```
   
### 5.Visit http://127.0.0.1:5000 in your browser.

### 🌍 Live Demo
Deployed at: https://theresumator.onrender.com

---


<img width="1366" height="675" alt="Screenshot (309)" src="https://github.com/user-attachments/assets/68ea89e9-9f7a-45f9-843a-af12994c8f0b" />
<img width="1366" height="669" alt="Screenshot (308)" src="https://github.com/user-attachments/assets/8abc3109-2a96-4ac9-b800-42aac1db38d1" />

