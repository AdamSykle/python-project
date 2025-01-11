pipeline {
    agent any

    environment {
        DOCKER_HOST = "tcp://localhost:2375" // Указываем адрес Docker-сервера
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/AdamSykle/python-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo "Building Docker container and installing dependencies"
                    // Запускаем контейнер с установкой зависимостей
                    sh 'docker run --rm -v $(pwd):/app -w /app python:3.12 bash -c "python -m venv venv && ./venv/bin/pip install -r requirements.txt"'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "Running tests"
                    sh './venv/bin/pytest'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo "Deploying the project"
                    // Деплой
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline succeeded!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
