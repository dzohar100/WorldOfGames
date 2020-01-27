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
        sh 'docker build ~/PycharmProjects/WorldOfGames -d'
      }
    }
    stage('Run') {
      steps {
        sh 'docker-compose up'
      }
    }
    stage('Test') {
      steps {
        sh 'python e2e.py'
      }
    }
    stage('Finalize') {
      steps {
        sh 'docker exec -it worldofgames_web bash'
      }
    }
  }
}
