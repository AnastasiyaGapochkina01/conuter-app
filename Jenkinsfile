def remote = [:] // dict
pipeline {
    agent any
    parameters {
        string(name: 'TAG', defaultValue: 'latest')
    }

    environment {
        REPO = 'anestesia01/counter'
        TOKEN = credentials('docker-token')
        HOST = '18.225.9.35'
        DOCKER_USER = 'anestesia01'
        GIT_URL = 'git@github.com:AnastasiyaGapochkina01/conuter-app.git'
        PRJ_DIR = '/var/www/project'
    }

    stages {
        stage('Configure credentials') {
            steps {
                withCredentials([sshUserPrivateKey(credentialId: 'jenkins-key', keyFileVariable: 'private_key', usernameVariable: 'username')]) {
                    script {
                        remote.name = "${env.HOST}"
                        remote.host = "${env.HOST}"
                        remote.user = "$username"
                        remote.identity = readFile "$private_key"
                        remote.allowAnyHosts = true
                    }
                }
            }
        }

        stage('Checkout repo') {
            steps {
                git branch: 'main', url: "${env.GIT_URL}", credentialId: 'jenkins-key'
            }
        }

        stage('Build and push') {
            steps {
                script {
                    sh """
                        docker login -u ${env.DOCKER_USER} -p ${env.TOKEN}
                        docker build -t ${env.REPO}:${params.TAG} ./
                        docker push ${env.REPO}:${params.TAG}
                        docker logout
                    """
                }
            }
        }

        //tests

        stage('Deploy') {
            steps {
                script {
                    sh """
                        scp compose.yml ${env.HOST}:${env.PRJ_DIR}
                        scp scripts/set_env.py ${env.HOST}:${env.PRJ_DIR}
                    """
                    sshCommand remote: remote, command: """
                        docker pull ${env.REPO}:${params.TAG}
                        cd ${env.PRJ_DIR}
                        python3 set_env.py
                        docker compose up -d
                    """
                }
            }
        }
    }
}
