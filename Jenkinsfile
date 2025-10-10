pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'saketh479/calculator:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/saketh1122/calc.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        def app = docker.image("${DOCKER_IMAGE}")
                        app.push()
                    }
                }
            }
        }

        stage('Deploy using Ansible') {
            steps {
                
                sh '''
                    /home/saketh/.local/bin/ansible-playbook -i /home/saketh/calc/hosts.ini /home/saketh/calc/deploy.yml
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline Succeeded!'
        }
        failure {
            echo '❌ Pipeline Failed!'
        }
    }
}

