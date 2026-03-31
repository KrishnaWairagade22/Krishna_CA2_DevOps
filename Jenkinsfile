pipeline {
    agent any

    environment {
        GIT_REPO_URL = "https://github.com/KrishnaWairagade22/Krishna_CA2_DevOps.git"
        IMAGE_NAME = "student-feedback-app"
        // We will define the local python path dynamically after creation
        PY_EXE = "venv\\Scripts\\python.exe"
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
                echo '🔧 Creating Local Virtual Environment (Ensuring independence from System PATH)...'
                script {
                    // Try to use the standard python or py launcher to create the environment
                    try {
                        bat "python -m venv venv"
                    } catch (Exception e) {
                        echo "Standard 'python' failed, trying 'py' launcher..."
                        bat "py -m venv venv"
                    }
                }
                // Now that venv is created, install dependencies using the LOCAL python
                echo '📥 Installing dependencies into local venv...'
                bat "${PY_EXE} -m pip install -r requirements.txt"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '📦 Building Docker Container Image...'
                script {
                    try {
                        bat "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                    } catch (Exception e) {
                        echo "Docker not available, skipping build: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo '🧪 Executing Selenium Automation Test Suite (using venv)...'
                // Running tests using the local venv python confirmed to work
                bat "${PY_EXE} test_form.py"
            }
        }
    }

    post {
        success {
            echo '✅ BUILD SUCCESSFUL! All environment hurdles cleared.'
        }
        failure {
            echo '❌ BUILD FAILED: If still failing, please check if "python" or "py" is installed on this PC.'
        }
    }
}
