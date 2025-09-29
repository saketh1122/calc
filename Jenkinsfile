pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/yourusername/devops-calculator.git'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }
    }
}
