# 🚀 Student Feedback Registration Form — DevOps Project

**Student:** Krishna Wairagade | **GitHub:** [KrishnaWairagade22/Krishna_CA2_DevOps](https://github.com/KrishnaWairagade22/Krishna_CA2_DevOps)

---

## 📌 Project Overview

A Student Feedback Registration Form built as a complete **end-to-end DevOps workflow**, demonstrating how modern software is developed, tested, containerized, and deployed using industry-standard DevOps tools.

---

## 🔄 DevOps Workflow (End-to-End)

```
Developer writes code
        ↓
Git commit + push to GitHub         [Version Control]
        ↓
Jenkins detects change              [CI/CD Automation]
        ↓
Selenium tests run automatically    [Automated Testing]
        ↓
Docker image is built               [Containerization]
        ↓
Container is deployed               [Delivery]
        ↓
App is LIVE at localhost:8081 ✅    [Running Application]
```

---

## 🛠️ Tools & Technologies

| Tool | Role | Aim |
|------|------|-----|
| **HTML/CSS/JS** | Web application (Student Feedback Form) | Aim 1 |
| **Git** | Local version control | Aim 2 |
| **GitHub** | Remote repository & collaboration | Aim 3 |
| **Selenium** | Automated UI testing | Aim 4/5 |
| **Jenkins** | CI/CD pipeline automation | Aim 5/6 |
| **Docker** | Containerization | Aim 6 |
| **Docker Compose** | Multi-container management | Aim 7 |
| **Docker + Jenkins** | CI triggers Docker build & deploy | Aim 8 |
| **All Together** | End-to-end pipeline | Aim 9/10 |

---

## 📁 Project Structure

```
Krishna_CA2_DevOps/
├── index.html              # Student Feedback Form (web app)
├── styles.css              # Styling
├── script.js               # JavaScript validation
├── test_form.py            # Selenium automated tests (7 test cases)
├── conftest.py             # Selenium/pytest configuration
├── requirements.txt        # Python dependencies
├── Jenkinsfile             # Jenkins CI/CD pipeline (9 stages)
├── Dockerfile              # Docker image build instructions
├── docker-compose.yml      # Multi-container app definition
└── .dockerignore           # Files excluded from Docker build
```

---

## ⚙️ Jenkins CI/CD Pipeline — 9 Stages

```
Stage 1 → Checkout              Pull latest code from GitHub
Stage 2 → Build                 Verify all app files exist
Stage 3 → Setup Venv            Create isolated Python environment
Stage 4 → Install Dependencies  pip install from requirements.txt
Stage 5 → Prepare Reports       Create test reports folder
Stage 6 → Run Selenium Tests    Execute all automated UI tests
Stage 7 → Deploy                Copy files to local server
Stage 8 → Docker Build Image    Build Docker image via Jenkins
Stage 9 → Docker Deploy         Run container on port 8081
```

---

## 🐳 Docker Setup

**Single container (Aim 6):**
```bash
docker build -t student-feedback-form:1.0 .
docker run -d -p 8081:80 --name feedback-app student-feedback-form:1.0
```

**Multi-container (Aim 7):**
```bash
docker compose up -d      # starts web + MySQL DB + Adminer (3 containers)
docker compose ps         # verify all running
docker compose down       # stop all
```

---

## 🧪 Running Tests Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run Selenium tests
pytest test_form.py -v

# Run with report
pytest test_form.py -v --junitxml=reports/result.xml
```

---

## 🚀 Quick Start — Run the App

```bash
# Clone the repo
git clone https://github.com/KrishnaWairagade22/Krishna_CA2_DevOps.git
cd Krishna_CA2_DevOps

# Run with Docker
docker build -t student-feedback-form:1.0 .
docker run -d -p 8081:80 --name feedback-app student-feedback-form:1.0

# Open in browser
# http://localhost:8081
```

---

## ✅ Verification Checklist

| Check | Command | Expected |
|-------|---------|----------|
| Docker image exists | `docker images` | `student-feedback-form` |
| Container running | `docker ps` | `feedback-app` — Up |
| App accessible | Browser | `http://localhost:8081` |
| Tests passing | `pytest test_form.py -v` | All green |
| Jenkins pipeline | `http://localhost:8080` | All 9 stages green |
