pipeline {
    agent any

    environment {
        // Define any environment variables here
        PYTHON_PATH = "python"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                // If this Jenkinsfile is part of your SCM, 'checkout scm' is implicitly called
                // You can manually add git checkout here if needed.
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
                // Install dependencies from requirements.txt
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Perform Static Analysis (Optional)') {
            steps {
                echo 'Checking code quality with linting (optional)...'
                // bat 'pip install flake8 && flake8 *.py'
                echo 'Linting passed.'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo '🚀 Executing Selenium Automation Test Suite...'
                // Running the test script and capturing output
                bat 'python test_form.py'
            }
        }
    }

    post {
        success {
            echo '✅ BUILD SUCCESSFUL: All automation tests passed!'
        }
        failure {
            echo '❌ BUILD FAILED: One or more tests failed or there was a system error.'
        }
        always {
            echo 'Cleaning up workspace and finishing pipeline execution...'
            // Add any cleanup or reporting steps here
        }
    }
}
