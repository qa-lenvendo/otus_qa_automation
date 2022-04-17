pipeline {
    agent any

    stages{
        stage('Git') {
            steps {
                echo "${BASE_URL}"
                git branch: 'jenkins', url: 'https://github.com/qa-lenvendo/otus_qa_automation.git'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t otus_tests . < Dockerfile'
            }
        }
        stage('Tests') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh """docker run --name test_run --network selenoid otus_tests --mode=remote --base_url=${BASE_URL} --browser_name=${BROWSER} --hub=${EXECUTOR_HUB} --hub_port=${EXECUTOR_PORT} && docker cp test_run:/app/allure-results ."""
                }
            }
        }
        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
    post {
        always {
            sh 'docker rm test_run'
        }
    }
}