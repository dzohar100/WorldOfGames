pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        sh 'git clone https://github.com/dzohar100/WorldOfGames'
      }
    }
    stage('Build') {
      steps {
        sh 'cd ~'
        sh 'docker build PycharmProjects/WorldOfGames'
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
