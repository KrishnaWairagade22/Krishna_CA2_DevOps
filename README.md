# Student Feedback Registration Form - DevOps Project

## Project Overview
This project is a Student Feedback Registration Form built as part of a DevOps CA2 assignment. It demonstrates a complete CI/CD pipeline integrated with automated Selenium testing.

## Technologies Used (The "Environment"):
- **Frontend**: HTML5, CSS3, JavaScript (with client-side validation).
- **Automation Testing**: Python with **Selenium WebDriver**.
- **CI/CD Pipeline**: **Jenkins** (using Declarative Pipeline).
- **Version Control**: **Git & GitHub**.

## Key Files:
- `index.html`: The main form.
- `script.js`: JavaScript validation logic.
- `test_form.py`: **Selenium automation test suite** (Includes 7 comprehensive test cases).
- `requirements.txt`: Python dependencies (Selenium, WebDriver Manager).
- `Jenkinsfile`: Defines the automated build and test pipeline.

## How to Set Up the Environment Locally:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/KrishnaWairagade22/Krishna_CA2_DevOps.git
   ```
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run tests manually**:
   ```bash
   python test_form.py
   ```

## Jenkins Pipeline Stages:
1. **Checkout**: Pulls the latest code from GitHub.
2. **Environment Setup**: Verifies Python and installs all dependencies from `requirements.txt`.
3. **Run Selenium Tests**: Executes automated tests in **headless mode** for stability in CI.
4. **Post-Build Actions**: Reports success or failure based on test results.
