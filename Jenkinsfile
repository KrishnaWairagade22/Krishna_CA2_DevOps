pipeline {
    agent any

    environment {
        // We will try several common Windows paths to find your Python automatically
        PY_LAUNCHER = "py" 
        PY_PATH = "python"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/KrishnaWairagade22/Krishna_CA2_DevOps.git'
            }
        }

        stage('Determine Python Path') {
            steps {
                script {
                    echo "🔍 Searching for your direct Python installation..."
                    // This block checks if python or py is available in the Jenkins service PATH
                    def pyStatus = bat(script: "python --version", returnStatus: true)
                    if (pyStatus == 0) {
                        echo "✅ Standard 'python' found!"
                        env.FINAL_PY = "python"
                    } else {
                        def launcherStatus = bat(script: "py --version", returnStatus: true)
                        if (launcherStatus == 0) {
                            echo "✅ 'py' launcher found!"
                            env.FINAL_PY = "py"
                        } else {
                            // If those FAIL (common in Jenkins services), we try common hardcoded paths
                            echo "⚠️ Standard commands failed. Trying absolute paths..."
                            def commonPaths = [
                                "C:\\Users\\krish\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe",
                                "C:\\Program Files\\PostgreSQL\\18\\pgAdmin 4\\python\\python.exe",
                                "D:\\SEM-1,2,3,4,5\\IBM -Seminar\\env1\\Scripts\\python.exe"
                            ]
                            def found = false
                            for (p in commonPaths) {
                                if (bat(script: "\"$p\" --version", returnStatus: true) == 0) {
                                    echo "🎯 Found Python at: $p"
                                    env.FINAL_PY = "\"$p\""
                                    found = true
                                    break
                                }
                            }
                            if (!found) {
                                error "❌ CRITICAL ERROR: Python is not found or not in System PATH for Jenkins. Please install Python and check 'Add to Path' for ALL USERS."
                            }
                        }
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                if exist venv rmdir /s /q venv
                ${env.FINAL_PY} -m venv venv
                call venv\\Scripts\\activate.bat
                pip install -r requirements.txt
                """
            }
        }

        stage('Execute Selenium Tests') {
            steps {
                bat """
                call venv\\Scripts\\activate.bat
                pytest test_form.py -v --junitxml=reports/result.xml
                """
            }
        }
    }

    post {
        always {
            // Keep your friend's reporting style
            junit 'reports/result.xml'
        }
        success {
            echo 'Build and Tests Passed Successfully!'
        }
        failure {
            echo 'Pipeline failed. Check determine stage to see if Python was found.'
        }
    }
}
