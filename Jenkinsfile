pipeline {
    agent any

    environment {
        // Full absolute path to python.exe — required because Jenkins runs as
        // SYSTEM service and cannot access the user's PATH
        PYTHON_EXE = "C:\\Users\\krish\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/KrishnaWairagade22/Krishna_CA2_DevOps.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                bat """
                    if exist venv rmdir /s /q venv
                    "${PYTHON_EXE}" -m venv venv
                """
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
