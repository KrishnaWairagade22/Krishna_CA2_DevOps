// Jenkinsfile - Student Feedback Registration Form
// Sub Task 5: Jenkins Pipeline Configuration

pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning the project repository...'
                // If using Git, uncomment and update the URL below:
                // git url: 'https://github.com/YOUR_USERNAME/Krishna_CA2_DevOps.git', branch: 'main'
                echo 'Repository cloned successfully.'
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat 'python --version'
                bat 'pip install selenium'
                echo 'Environment setup complete.'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Running Selenium test cases...'
                bat 'python test_form.py'
                echo 'Selenium tests completed.'
            }
        }
    }

    post {
        success {
            echo '✅ BUILD SUCCESSFUL: All Selenium tests passed!'
        }
        failure {
            echo '❌ BUILD FAILED: One or more Selenium tests failed.'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
