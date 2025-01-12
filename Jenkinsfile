dpipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AdamSykle/python-project.git', credentialsId: 'github-credentials'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    docker.withServer('tcp://localhost:2375') {
                        docker.image('python:3.12.2').inside {
                            bat 'pip install -r requirements.txt'
                        }
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.withServer('tcp://localhost:2375') {
                        docker.image('python:3.12.2').inside {
                            bat 'pytest'
                        }
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
