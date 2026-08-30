pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Code has been checked out by Jenkins.'
            }
        }

        stage('Run Application') {
            steps {
                sh 'python3 app.py'
            }
        }

    }
}
