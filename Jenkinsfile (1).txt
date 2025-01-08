pipeline {
    agent any

    stages {
        stage('Environment Setup') {
            steps {
                script {
                    bat '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
            post {
                always {
                    // Update GitHub status for setup stage
                    step([$class: 'GitHubCommitStatusSetter',
                          contextSource: [$class: 'ManuallyEnteredCommitContextSource', context: 'Environment Setup'],
                          statusResultSource: [$class: 'ConditionalStatusResultSource', results: [
                              [$class: 'AnyBuildResult', state: 'SUCCESS', message: 'Environment setup completed successfully.'],
                              [$class: 'AnyBuildResult', state: 'FAILURE', message: 'Environment setup encountered an issue.']
                          ]]
                    ])
                }
            }
        }

        stage('Execute Tests') {
            steps {
                script {
                    bat '''
                    pytest tests/
                    '''
                }
            }
            post {
                always {
                    // Update GitHub status for test execution
                    step([$class: 'GitHubCommitStatusSetter',
                          contextSource: [$class: 'ManuallyEnteredCommitContextSource', context: 'Test Execution'],
                          statusResultSource: [$class: 'ConditionalStatusResultSource', results: [
                              [$class: 'AnyBuildResult', state: 'SUCCESS', message: 'All tests passed successfully.'],
                              [$class: 'AnyBuildResult', state: 'FAILURE', message: 'Test execution encountered failures.']
                          ]]
                    ])
                }
            }
        }
    }

    post {
        failure {
            // Notify GitHub of pipeline failure
            step([$class: 'GitHubCommitStatusSetter',
                  contextSource: [$class: 'ManuallyEnteredCommitContextSource', context: 'Pipeline Status'],
                  statusResultSource: [$class: 'ConditionalStatusResultSource', results: [
                      [$class: 'AnyBuildResult', state: 'FAILURE', message: 'The pipeline did not complete successfully.']
                  ]]
            ])
            // Send email notification for failed build
            emailext (
                subject: "Pipeline Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                The build #${env.BUILD_NUMBER} for the job ${env.JOB_NAME} has failed.

                Check the details here: ${env.BUILD_URL}

                Regards,
                Jenkins Pipeline
                """,
                to: "developer@example.com",
                recipientProviders: [[$class: 'CulpritsRecipientProvider'], [$class: 'DevelopersRecipientProvider']]
            )
        }

        success {
            // Notify GitHub of pipeline success
            step([$class: 'GitHubCommitStatusSetter',
                  contextSource: [$class: 'ManuallyEnteredCommitContextSource', context: 'Pipeline Status'],
                  statusResultSource: [$class: 'ConditionalStatusResultSource', results: [
                      [$class: 'AnyBuildResult', state: 'SUCCESS', message: 'Pipeline executed successfully.']
                  ]]
            ])
            echo 'Pipeline completed successfully!'
        }
    }
}
