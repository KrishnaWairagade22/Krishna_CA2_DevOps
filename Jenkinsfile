pipeline {
    agent any

    environment {
        // Full absolute path to python.exe — required because Jenkins runs as
        // SYSTEM service and cannot access the user's PATH
        PYTHON_EXE  = "C:\\Users\\krish\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"

        // Deployment target folder (simulates a local web server document root)
        DEPLOY_DIR  = "C:\\DeployedApp\\StudentFeedbackForm"

        // Application version tag (build number is injected by Jenkins automatically)
        APP_VERSION = "1.0.${BUILD_NUMBER}"
    }

    stages {

        // ─────────────────────────────────────────────
        // STAGE 1 — CI: Pull latest code from GitHub
        // ─────────────────────────────────────────────
        stage('Checkout') {
            steps {
                echo "Checking out source code — version ${APP_VERSION}"
                git branch: 'master', url: 'https://github.com/KrishnaWairagade22/Krishna_CA2_DevOps.git'
            }
        }

        // ─────────────────────────────────────────────
        // STAGE 2 — CI: Verify the build (all app files present)
        // ─────────────────────────────────────────────
        stage('Build') {
            steps {
                echo 'Verifying application build artifacts...'
                bat '''
                    echo Build version: %APP_VERSION%
                    echo Checking required files...
                    if not exist index.html (echo [ERROR] index.html missing & exit /b 1)
                    if not exist styles.css (echo [ERROR] styles.css missing & exit /b 1)
                    if not exist script.js  (echo [ERROR] script.js missing  & exit /b 1)
                    echo [OK] index.html found
                    echo [OK] styles.css found
                    echo [OK] script.js found
                    echo Build verification complete.
                '''
            }
        }

        // ─────────────────────────────────────────────
        // STAGE 3 — CI: Set up isolated Python environment
        // ─────────────────────────────────────────────
        stage('Setup Virtual Environment') {
            steps {
                bat """
                    if exist venv rmdir /s /q venv
                    "${PYTHON_EXE}" -m venv venv
                """
            }
        }

        // ─────────────────────────────────────────────
        // STAGE 4 — CI: Install test dependencies
        // ─────────────────────────────────────────────
        stage('Install Dependencies') {
            steps {
                bat '''
                    venv\\Scripts\\pip install --upgrade pip
                    venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        // ─────────────────────────────────────────────
        // STAGE 5 — CI: Prepare reports folder
        // ─────────────────────────────────────────────
        stage('Prepare Reports Directory') {
            steps {
                bat '''
                    if not exist reports mkdir reports
                '''
            }
        }

        // ─────────────────────────────────────────────
        // STAGE 6 — CI: Run all Selenium automated tests
        // ─────────────────────────────────────────────
        stage('Run Selenium Tests') {
            steps {
                bat '''
                    venv\\Scripts\\pytest test_form.py -v --junitxml=reports/result.xml --tb=short
                '''
            }
        }

        // ─────────────────────────────────────────────
        // STAGE 7 — CD: Deploy app to local server folder
        // Only runs if ALL previous CI stages passed
        // ─────────────────────────────────────────────
        stage('Deploy') {
            steps {
                echo "Deploying version ${APP_VERSION} to ${DEPLOY_DIR}"
                bat """
                    :: Create deployment directory if it doesn't exist
                    if not exist "${DEPLOY_DIR}" mkdir "${DEPLOY_DIR}"

                    :: Copy application files to deployment folder
                    copy /Y index.html  "${DEPLOY_DIR}\\index.html"
                    copy /Y styles.css  "${DEPLOY_DIR}\\styles.css"
                    copy /Y script.js   "${DEPLOY_DIR}\\script.js"

                    :: Write a deployment info file for traceability
                    echo Build: %APP_VERSION%          >  "${DEPLOY_DIR}\\deployment-info.txt"
                    echo Date: %DATE% %TIME%           >> "${DEPLOY_DIR}\\deployment-info.txt"
                    echo Source: GitHub master branch  >> "${DEPLOY_DIR}\\deployment-info.txt"
                    echo Status: Deployed Successfully >> "${DEPLOY_DIR}\\deployment-info.txt"

                    echo [SUCCESS] Application deployed to ${DEPLOY_DIR}
                    echo Files in deployment directory:
                    dir "${DEPLOY_DIR}"
                """
            }
        }

        // ─────────────────────────────────────────────
        // STAGE 8 — AIM 8: Build Docker Image via CI
        // Jenkins builds a Docker image automatically
        // after tests pass — this is CI + Docker integration
        // ─────────────────────────────────────────────
        stage('Docker Build Image') {
            steps {
                echo "Building Docker image: student-feedback-form:${APP_VERSION}"
                bat """
                    docker build -t student-feedback-form:${APP_VERSION} .
                    echo [SUCCESS] Docker image built: student-feedback-form:${APP_VERSION}
                    docker images student-feedback-form
                """
            }
        }

        // ─────────────────────────────────────────────
        // STAGE 9 — AIM 8: Deploy Docker Container via CI
        // Jenkins stops old container (if any) and runs
        // a fresh container from the newly built image
        // ─────────────────────────────────────────────
        stage('Docker Deploy Container') {
            steps {
                echo "Deploying Docker container from image student-feedback-form:${APP_VERSION}"
                bat """
                    :: Stop and remove old container if it exists
                    docker stop feedback-app 2>nul || echo No old container to stop
                    docker rm   feedback-app 2>nul || echo No old container to remove

                    :: Run fresh container from the newly built image
                    docker run -d -p 8081:80 --name feedback-app student-feedback-form:${APP_VERSION}

                    echo [SUCCESS] Container is running!
                    docker ps --filter name=feedback-app
                """
            }
        }
    }

    post {
        always {
            // Always publish test results as a Jenkins report
            junit allowEmptyResults: true, testResults: 'reports/result.xml'

            // Archive app files + reports as downloadable Jenkins artifacts
            archiveArtifacts artifacts: 'index.html, styles.css, script.js, reports/result.xml',
                             allowEmptyArchive: true,
                             fingerprint: true
        }
        success {
            echo "CI/CD Pipeline PASSED — Version ${APP_VERSION} deployed successfully!"
        }
        failure {
            echo "CI/CD Pipeline FAILED — Deployment was skipped. Fix test errors and retry."
        }
    }
}
