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
        sh 'docker-compose up -d'
      }
    }
    stage('Test') {
      steps {
        sh 'python3 e2e.py'
      }
    }
    stage('Finalize') {
      steps {
        sh 'docker exec 67ba1e52f50d sh'
      }
    }
  }
}
