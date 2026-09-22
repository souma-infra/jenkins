pipeline{
	agent any 
	environment {
		APP_NAME = "jenkins-app-demo"
		BUILD_TAG_CUSTOM = "jenkins-app-demo-${env.BUILD_NUMBER}"
	}
	stages {
		stage('Build'){
			steps {
				echo "Building application ${env.APP_NAME}"
				echo "installing dependencies from requirements.txt"
				sh 'pip3 install -r requirements.txt'
			}
		}
		stage('Test'){
			steps {
				echo "Testing the application ${env.APP_NAME}"
				sh 'pytest testing.py --junitxml=results.xml'
			}
		}
		stage('Approval'){
			steps {
				echo "waiting for the approval to deploy the application ${env.APP_NAME}"
				input message: "Do you want to deploy the ${env.APP_NAME} app to production ?"
			}
		}
		stage('Deploy'){
			steps{
				echo "Deploying the application ${env.APP_NAME} to production"
				sh 'echo "Deploying the application to production"'
			}
		}
	}
	post {
        	always {
            		echo "Pipeline finished for build #${BUILD_NUMBER}"
            		junit 'results.xml'
        	}
        	success {
            		echo "Build ${BUILD_TAG_CUSTOM} succeeded."
					echo "Deploy successful for the application ${env.APP_NAME} to production environment."
       	        }
        	failure {
            		echo "Build ${BUILD_TAG_CUSTOM} failed. Check the Test stage output above."
					echo "Deployment was not successful for the application ${env.APP_NAME} to production environment."
        	}
    	}
}
