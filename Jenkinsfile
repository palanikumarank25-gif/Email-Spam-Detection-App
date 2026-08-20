pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Gaming\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\Gaming\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m py_compile app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t email-spam-detection-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker stop email-spam-container || exit 0'
                bat 'docker rm email-spam-container || exit 0'
                bat 'docker run -d -p 8501:8501 --name email-spam-container email-spam-detection-app'
            }
        }
    }

    post {
        success {
            echo 'Email Spam Detection CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
