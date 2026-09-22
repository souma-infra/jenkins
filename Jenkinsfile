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
				sh 'pip3 install -r requirements.txt'
			}
		}
		stage('Test'){
			steps {
				echo "Testing the application ${env.APP_NAME}"
				sh 'pytest testing.py --junitxml=results.xml'
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
       	        }
        	failure {
            		echo "Build ${BUILD_TAG_CUSTOM} failed. Check the Test stage output above."
        	}
    	}

}
