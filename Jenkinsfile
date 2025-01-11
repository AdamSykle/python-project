pipeline {

    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AdamSykle/python-project.git', credentialsId: 'jafar01-dockerhub'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    docker.image('python:3.12').inside {
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image('python:3.12').inside {
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying the project..."
                // Здесь можно добавить команды для деплоя, если потребуется
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
