from flask import Flask, render_template, request
import PyPDF2, docx, re
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# --- PDF Extraction ---
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# --- DOCX Extraction ---
def extract_text_from_docx(file):
    doc = docx.Document(file)
    return '\n'.join([para.text for para in doc.paragraphs])

# --- Name Extraction ---
def extract_name(text):
    lines = text.strip().split('\n')[:5]  # First 5 lines
    doc = nlp(' '.join(lines))
    for ent in doc.ents:
        if ent.label_ == 'PERSON' and ent.text.strip().lower() not in ['resume', 'tamil nadu', 'india']:
            return ent.text.strip()
    return "Not Found"

# --- Skills Extraction ---
def extract_skills(text):
    known_skills = ['Python', 'Django', 'React', 'Flask', 'MySQL', 'HTML', 'CSS', 'JavaScript', 'Git', 'Bootstrap']
    matched = []
    missing = []
    for skill in known_skills:
        if skill.lower() in text.lower():
            matched.append(skill)
        else:
            missing.append(skill)
    return matched, missing

# --- Experience Extraction ---
def extract_experience(text):
    experience_keywords = [
        r'(\d+)\+?\s*(years|yrs)\s+of\s+(experience|internship)',
        r'(\d+)\+?\s*(years|yrs)\s+(experience|internship)',
        r'(\d+)\s*(years|yrs)'
    ]
    for pattern in experience_keywords:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(0)
    if "internship" in text.lower():
        return "Internship (duration not specified)"
    return "Not Found"

# --- Info Extractor ---
def extract_info(text):
    lines = [line.strip() for line in text.split('\n') if line.strip()]

    # ---- NAME Extraction ----
    name = "Not Found"
    for line in lines:
        if line.lower().startswith("name:"):
            name = line.split(":", 1)[1].strip()
            break
    if name == "Not Found":
        first_line = lines[0]
        blacklist = ['resume', 'cv', 'curriculum vitae', 'profile']
        if not any(bad in first_line.lower() for bad in blacklist):
            name = first_line

    # ---- EMAIL Extraction ----
    email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

    # ---- PHONE Extraction ----
    phone = re.findall(r'\+?\d[\d\s-]{8,13}', text)

    # ---- SKILLS Extraction ----
    known_skills = ['Python', 'Django', 'Flask', 'React', 'MySQL', 'HTML', 'CSS', 'JavaScript', 'C', 'C++', 'Git', 'Bootstrap']
    parsed_skills = [skill for skill in known_skills if skill.lower() in text.lower()]
    required_skills = list(set(known_skills) - set(parsed_skills))

    # ---- EXPERIENCE Extraction ----
    exp_keywords = ['experience', 'internship', 'intern', 'worked at', 'role', 'responsibilities', 'project']
    experience = "Not Found"
    for line in lines:
        if any(keyword in line.lower() for keyword in exp_keywords) and len(line.split()) >= 5:
            experience = line.strip()
            break

    return {
        "name": name,
        "email": email[0] if email else "Not Found",
        "phone": phone[0] if phone else "Not Found",
        "skills": parsed_skills,
        "missing_skills": required_skills,
        "experience": experience
    }


# --- Flask Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['resume']
        if file.filename.endswith('.pdf'):
            text = extract_text_from_pdf(file)
        elif file.filename.endswith('.docx'):
            text = extract_text_from_docx(file)
        else:
            return "Unsupported file type. Please upload a PDF or DOCX."
        
        data = extract_info(text)
        return render_template('result.html', data=data)

    return render_template('index.html')

# --- Main ---
if __name__ == '__main__':
    app.run(debug=True)
