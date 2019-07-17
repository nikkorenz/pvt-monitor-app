pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'sudo docker run hello-world'
      }
    }
  }
  environment {
    test = 'test'
  }
}