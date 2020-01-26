pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        echo 'Hello'
      }
    }
    stage('Build') {
      steps {
        sh 'docker build ~/PycharmProjects/WorldOfGames'
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
