pipeline {
    agent any

    environment {
        // Установка переменных окружения (например, версия Python)
        PYTHON_VERSION = '3.12.2'
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
                    // Установка зависимостей с использованием pip
                    echo "Installing dependencies"
                    sh 'python -m venv venv'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Запуск тестов, например, с использованием pytest
                    echo "Running tests"
                    bat '.\\venv\\Scripts\\pytest'
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
