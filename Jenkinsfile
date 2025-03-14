pipeline {
    agent any
    
    environment {
        PYTHON = "python3"
        ALLURE_RESULTS = "allure-results"  // Місце для збереження результатів Allure
        ALLURE_REPORT = "allure-report"    // Місце для збереження звіту Allure
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
                // Запуск тестів з Allure та збереження результатів
                sh './venv/bin/pytest --alluredir=${ALLURE_RESULTS} --junitxml=reports/results.xml'
            }
        }
        
        stage('Publish Test Results') {
            steps {
                // Публікація результатів тестів у форматі JUnit
                junit 'reports/results.xml'
                
                // Генерація звіту Allure
                allure includeProperties: false, jdk: '', results: [[path: '${ALLURE_RESULTS}']]
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
