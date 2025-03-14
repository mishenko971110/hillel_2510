pipeline {
    agent any
    
    environment {
        PYTHON = "python3"
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/mishenko971110/hillel_2510'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '${PYTHON} -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh './venv/bin/pytest --junitxml=reports/results.xml'
            }
        }
        
        stage('Publish Test Results') {
            steps {
                junit 'reports/results.xml'
            }
        }
    }
    
    post {
        always {
            emailext subject: "Jenkins Build: ${currentBuild.fullDisplayName}",
                     body: "Build ${currentBuild.fullDisplayName} finished with status: ${currentBuild.currentResult}",
                     recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                     to: 'mishenko971110@gmail.com'
        }
    }
}
