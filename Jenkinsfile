pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git checkout 
      }}
    stage('Build') {
      steps {
        docker build /Users/DorZohar 1/PycharmProjects/WorldOfGames/Dockerfile
      }}
    stage('Run') {
      steps {
        docker run --name wog -p 8777:8777 -d
      }}
    stage('Test') {
      steps {
        sh 'python e2e.py'
      }}
    stage('Finalize') {
      steps {
        docker exec -it wog bash
      }}}}
