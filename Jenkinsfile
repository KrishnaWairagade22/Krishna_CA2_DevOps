pipeline {
    agent any

    environment {
        // TIP: If 'python' is not found, change this to your full path:
        // Example: PYTHON_PATH = "C:\\Users\\YourName\\AppData\\Local\\Programs\\Python\\Python39\\python.exe"
        PYTHON_PATH = "python" 
        IMAGE_NAME = "student-feedback-app"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '🚀 Pulling the latest code from GitHub...'
                // Explicitly pull the source code into the workspace
                checkout scm
                
                script {
                    echo 'Current Workspace Contents:'
                    if (isUnix()) {
                        sh 'ls -la'
                    } else {
                        bat 'dir'
                    }
                }
            }
        }

        stage('Environment Setup') {
            steps {
                echo '🔧 Setting up Python environment...'
                script {
                    try {
                        bat "${PYTHON_PATH} --version"
                    } catch (Exception e) {
                        echo "Standard 'python' command failed, trying 'py' launcher..."
                        env.PYTHON_PATH = "py"
                        bat "${env.PYTHON_PATH} --version"
                    }
                }
                // Install dependencies from requirements.txt
                bat "${env.PYTHON_PATH} -m pip install -r requirements.txt"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '📦 Building Docker Container Image...'
                script {
                    try {
                        bat "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                    } catch (Exception e) {
                        echo "Docker not available, skipping build stage: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo '🧪 Executing Selenium Automation Test Suite...'
                // Running the test script using the verified Python path
                bat "${env.PYTHON_PATH} test_form.py"
            }
        }
    }

    post {
        success {
            echo '✅ BUILD SUCCESSFUL!'
        }
        failure {
            echo '❌ BUILD FAILED: Check the logs above for the error (usually Python path or missing dependencies).'
        }
        always {
            echo 'Finishing pipeline execution...'
        }
    }
}
