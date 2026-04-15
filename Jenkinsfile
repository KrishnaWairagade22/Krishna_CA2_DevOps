pipeline {
    agent any

    environment {
        PYTHON = "python"
        REPORTS_DIR = "reports"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/KrishnaWairagade22/Krishna_CA2_DevOps.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                bat '''
                    if exist venv rmdir /s /q venv
                    python -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    venv\\Scripts\\pip install --upgrade pip
                    venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        stage('Prepare Reports Directory') {
            steps {
                bat '''
                    if not exist reports mkdir reports
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat '''
                    venv\\Scripts\\pytest test_form.py -v --junitxml=reports/result.xml --tb=short
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/result.xml'
        }
        success {
            echo 'All tests passed successfully!'
        }
        failure {
            echo 'Some tests failed. Check the console output and reports for details.'
        }
    }
}
