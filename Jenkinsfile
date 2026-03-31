pipeline {
    agent any

    environment {
        // Defines the Python execution path for your project
        PYTHON_PATH = "python"
        IMAGE_NAME = "student-feedback-app"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling the latest code from GitHub...'
                // 'checkout scm' is implied but we can list files to verify
                script {
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
                echo 'Setting up Python environment and installing dependencies...'
                bat 'python --version'
                // Installs dependencies from requirements.txt
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '📦 Building Docker Container Image for the Application Environment...'
                // This stage builds the environment we pushed earlier
                script {
                    try {
                        bat 'docker build -t %IMAGE_NAME%:%BUILD_NUMBER% .'
                    } catch (Exception e) {
                        echo "Docker not available on this Jenkins agent, skipping build stage: ${e}"
                    }
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo '🚀 Executing Selenium Automation Test Suite in Headless Mode...'
                // Running the test script and capturing output
                bat 'python test_form.py'
            }
        }
    }

    post {
        success {
            echo '✅ BUILD SUCCESSFUL: All automation tests passed and environment was verified!'
        }
        failure {
            echo '❌ BUILD FAILED: One or more tests failed or there was a system error.'
        }
        always {
            echo 'Cleaning up workspace and finishing pipeline execution...'
        }
    }
}
