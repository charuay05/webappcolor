pipeline {
  agent any
  
  triggers {
    pollSCM '* * * * *'
  }

  stages {
    stage('Build') {
      steps {
        sh "docker build -t dockerkawao/simple-web-app:${env.BUILD_NUMBER} ."
      }
    }
    stage('Release') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh "docker push dockerkawao/simple-web-app:${env.BUILD_NUMBER}"
          sh "docker rmi dockerkawao/simple-web-app:${env.BUILD_NUMBER}"
        }
      }
    }
    stage('Deploy') {
      steps {
          withKubeConfig([credentialsId: 'kubeconfig']) {
          sh 'cat color-deployment.yaml | sed "s/{{BUILD_NUMBER}}/$BUILD_NUMBER/g" | kubectl apply -f -'
          sh 'kubectl apply -f color-service.yaml'
        }
      }
    }
  }
  post {
    success {
      slackSend(message: "Pipeline is successfully completed.")
    }
    failure {
      slackSend(message: "Pipeline failed. Please check the logs. http://localhost:8080/job/cicd1/${BUILD_NUMBER}")
    }
  }
}