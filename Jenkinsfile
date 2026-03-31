pipeline {
    agent any

    environment {
        // --- MANDATORY ACTION: CHANGE THIS PATH ---
        // 1. Run 'where python' in your CMD.
        // 2. Paste the result here. Note the double backslashes \\
        PYTHON_EXE = "C:\\Users\\krish\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" 
        
        GIT_REPO_URL = "https://github.com/KrishnaWairagade22/Krishna_CA2_DevOps.git"
        IMAGE_NAME = "student-feedback-app"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '🚀 Cloning the latest code from GitHub...'
                git url: "${GIT_REPO_URL}", branch: 'master'
            }
        }

        stage('Environment Setup') {
            steps {
                echo '🔧 Creating Local Virtual Environment...'
                script {
                    try {
                        // Using your direct system path to create the venv
                        bat "\"${PYTHON_EXE}\" -m venv venv"
                    } catch (Exception e) {
                        echo "Failed to create venv using ${PYTHON_EXE}. Error: ${e.getMessage()}"
                        error "BUILD ABORTED: Please check if the PYTHON_EXE path in the Jenkinsfile is correct."
                    }
                }
                echo '📥 Installing dependencies into local venv...'
                bat "venv\\Scripts\\python.exe -m pip install -r requirements.txt"
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo '🧪 Executing Selenium Automation Test Suite...'
                bat "venv\\Scripts\\python.exe test_form.py"
            }
        }
    }

    post {
        success {
            echo '✅ BUILD SUCCESSFUL!'
        }
        failure {
            echo '❌ BUILD FAILED: Check folder permissions or Python path.'
        }
    }
}
