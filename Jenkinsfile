pipeline {
    agent any

    environment {
        DOCKER_USER = "bharanisree40"
        IMAGE_NAME = "myapp2"
        IMAGE_TAG = "latest"
        IMAGE_FULL_NAME = "${DOCKER_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
    }

    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_FULL_NAME} ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker push ${DOCKER_USER}/${IMAGE_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }
    } // ← This was missing!

    post {
        success {
            echo "✅ Build and push successful!"
        }
        failure {
            echo "❌ Build or push failed."
        }
    }
}
