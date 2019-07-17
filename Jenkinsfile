pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'docker run hello-world'
      }
    }
  }
  environment {
    test = 'test'
  }
}