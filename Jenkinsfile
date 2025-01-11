pipeline {
    agent any  // Это использует любой доступный агент Jenkins

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/AdamSykle/python-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    docker.image('python:3.12').inside {
                        bat 'python -m venv venv'
                        bat './venv/bin/pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image('python:3.12').inside {
                        bat './venv/bin/pytest'
                    }
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
