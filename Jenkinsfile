pipeline {
    agent any

    environment {
        // Установка переменных окружения (например, версия Python)
        PYTHON_VERSION = '3.12.2'
        DOCKER_IMAGE = 'python:3.12'
    }

    stages {
        stage('Checkout') {
            steps {
                // Получаем исходный код из репозитория
                git 'https://github.com/AdamSykle/python-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Устанавливаем зависимости с использованием Docker
                    echo "Building Docker container and installing dependencies"
                    if (isUnix()) {
                        sh 'docker run --rm -v ${PWD}:/app -w /app ${DOCKER_IMAGE} bash -c "python -m venv venv && ./venv/bin/pip install -r requirements.txt"'
                    } else {
                        bat 'docker run --rm -v %CD%:/app -w /app %DOCKER_IMAGE% bash -c "python -m venv venv && ./venv/Scripts/pip install -r requirements.txt"'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Запуск тестов с использованием Docker
                    echo "Running tests"
                    if (isUnix()) {
                        sh 'docker run --rm -v ${PWD}:/app -w /app ${DOCKER_IMAGE} bash -c "./venv/bin/pytest"'
                    } else {
                        bat 'docker run --rm -v %CD%:/app -w /app %DOCKER_IMAGE% bash -c ".\\venv\\Scripts\\pytest"'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Деплой проекта (например, на сервер или в контейнер)
                    echo "Deploying the project"
                    // Здесь может быть команда для деплоя
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
