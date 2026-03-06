pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = 'scientific-calculator'
        GITHUB_REPO_URL = 'https://github.com/AsutoshAssignment/Calculator_SPE.git'
        DOCKER_HUB_USERNAME = 'asutoshassignment'
        LANG = 'en_US.UTF-8'
        LC_ALL = 'en_US.UTF-8'
    }

    stages {
        stage('Clone Git') {
            steps {
                script {
                    git branch: 'main',
                        url: "${GITHUB_REPO_URL}"
                }
            }
        }


        stage('Install Dependencies') {
    steps {
        sh '''
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        '''
    }
}

stage('Test the Project') {
    steps {
        sh '''
        source venv/bin/activate
        pytest
        '''
    }
}

        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE_NAME}", '.')
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', 'docker-hub-credential') {
                        sh "docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest"
                        sh "docker push ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest"
                    }
                }
            }
        }
        stage('Deploy with Ansible') {
            steps {
                script {
                    sh 'ansible-playbook -i inventory deploy.yml'
                }
            }
        }


post {

    success {
        emailext(
            subject: "SUCCESS: Jenkins Build ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: """
            Build Status: SUCCESS

            Job Name: ${env.JOB_NAME}
            Build Number: ${env.BUILD_NUMBER}
            Build URL: ${env.BUILD_URL}

            Docker Image Pushed: ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest
            """,
            to: "your-email@gmail.com",
            attachLog: true
        )
    }

    failure {
        emailext(
            subject: "FAILED: Jenkins Build ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: """
            Build Status: FAILED

            Job Name: ${env.JOB_NAME}
            Build Number: ${env.BUILD_NUMBER}

            Check console output:
            ${env.BUILD_URL}
            """,
            to: "your-email@gmail.com",
            attachLog: true
        )
    }

    }

    }
}
