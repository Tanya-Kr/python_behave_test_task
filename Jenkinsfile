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
                sh "pwd"
                sh "ls -a"
                sh "docker build -t behave ."
            }
        }

        stage('Run Image') {
            steps {
                script {
                    sh "docker run --rm behave"
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
//
// node {
//   git 'https://github.com/Tanya-Kr/python_behave_test_task.git/'
//   def myEnv = docker.build 'behave'
//   myEnv.inside {
//     sh 'docker run --rm --shm-size="6gb" behave'
//     sh "docker rmi behave"
//   }
// }
//
// node {
//      agent {
//             label 'docker'
//      }
//
//      stage('Clone repository') {
//         checkout scm
//      }
//
//      stage('Build Image') {
// //         docker.build('behave')
//         sh "docker build -t behave ."
//      }
//
//      stage('Run Image') {
//         sh "docker run --rm --shm-size="6gb" behave"
//      }
//
//      stage('Delete Image') {
//         sh "docker rmi behave"
//      }
// }
