pipeline {
    agent { 
        node {
            label 'docker-agent-python'
        }
    }
    triggers {
        pollSCM "* * * * *"
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                echo Build stage triggered ..
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd app
                python3 app.py
                python3 app.py --name=Celia
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "Done ✅✅"
                '''
            }
        }
    }
}