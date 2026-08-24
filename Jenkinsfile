pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
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

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    bat 'docker login -u "%DOCKER_USERNAME%" -p "%DOCKER_PASSWORD%"'
                    bat 'docker tag email-spam-detection-app %DOCKER_USERNAME%/email-spam-detection-app:latest'
                    bat 'docker push %DOCKER_USERNAME%/email-spam-detection-app:latest'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker stop email-spam-container || exit 0'
                bat 'docker rm email-spam-container || exit 0'
                bat 'docker run -d -p 8502:8501 --name email-spam-container email-spam-detection-app'
            }
        }  

        stage('Deploy to Kubernetes') { 
            steps { 
                bat 'kubectl apply -f deployment.yml'
                bat 'kubectl apply -f service.yml'
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
