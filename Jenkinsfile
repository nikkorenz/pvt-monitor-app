pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        dockerNode(image: 'nginx', connector: '80', dockerHost: 'localhost')
      }
    }
  }
}