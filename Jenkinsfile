pipeline {
    agent any

    environment {
        // Updated to use your 'krish' path. If you have a different version than 312, 
        // you only need to change that number here.
        PATH = "C:\\Users\\krish\\AppData\\Local\\Programs\\Python\\Python312\\;${env.WORKSPACE}\\venv\\Scripts\\;${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                // Pointing to YOUR repository and branch
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
