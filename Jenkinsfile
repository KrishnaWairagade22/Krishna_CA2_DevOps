pipeline {
    agent any

    environment {
        // Updated to use your actual user folder 'krish' to fix the path error
        PATH = "C:\\Users\\krish\\AppData\\Local\\Programs\\Python\\Python312\\;${env.WORKSPACE}\\venv\\Scripts\\;${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/KrishnaWairagade22/Krishna_CA2_DevOps.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                if exist venv rmdir /s /q venv
                python -m venv venv
                call venv\\Scripts\\activate.bat
                pip install -r requirements.txt
                '''
            }
        }

        stage('Execute Selenium Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                pytest test_form.py -v --junitxml=reports/result.xml
                '''
            }
        }
    }

    post {
        always {
            // This will show your test results graph in Jenkins
            junit 'reports/result.xml'
        }
        success {
            echo 'Build and Tests Passed Successfully!'
        }
        failure {
            echo 'Some Tests or Builds Failed. Check the log for details.'
        }
    }
}
