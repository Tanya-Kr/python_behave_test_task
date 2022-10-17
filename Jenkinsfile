pipeline {
    agent {
        label 'docker'
    }

    stages {
        stage('Clone repository') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                sh "docker build -t behave ."
            }
        }

        stage('Run Image') {
            steps {
                script {
                    sh "docker run --rm --shm-size='8gb' behave"
                }

            }
        }

        stage('Delete Image') {
            steps {
                sh "docker rmi behave"
            }
        }

    }
}