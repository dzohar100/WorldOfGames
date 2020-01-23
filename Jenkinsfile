pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        sh 'echo hello'
      }
    }
    stage('Build') {
      steps {
        sh 'docker build https://github.com/dzohar100/WorldOfGames/blob/master/Dockerfile .'
      }
    }
    stage('Run') {
      steps {
        sh 'docker run --name wog -p 8777:8777 -d'
      }
    }
    stage('Test') {
      steps {
        sh 'python e2e.py'
      }
    }
    stage('Finalize') {
      steps {
        sh 'docker exec -it wog bash'
      }
    }
  }
}
