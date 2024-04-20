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
                cd app
                pip install fire@0.4.0
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