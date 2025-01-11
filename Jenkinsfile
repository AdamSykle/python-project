pipeline {
    agent {
        docker {
            image 'python:3.12'  // Используем официальный образ с Python
            label 'linux'        // Если нужно, укажи лейбл для специфической машины (например, если ты используешь агенты Jenkins)
        }
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
                    echo "Installing dependencies"
                    sh 'python -m venv venv'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "Running tests"
                    sh './venv/bin/pytest test_app.py'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo "Deploying the project"
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
