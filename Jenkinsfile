pipeline {
    agent any
    environment {
        
        GITHUB_REPO_URL = 'https://github.com/AsutoshAssignment/Calculator_SPE.git'

    }

    stages {
        stage('Clone Git') {
            steps {
                script {
                    git branch: 'master',
                        url: "${GITHUB_REPO_URL}"
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install pytest'
            }
        }

        stage('Test the Project') {
            steps {
                sh 'pytest test_calculator.py'
            }
        }

        
}
