pipeline {
  agent any

  stages {
    stage('Build Producer') {
      steps {
        dir('producer') {
          sh 'docker build -t 192.168.64.12:5000/producer:latest .'
          sh 'docker push 192.168.64.12:5000/producer:latest'
        }
      }
    }

    stage('Build Worker') {
      steps {
        dir('worker') {
          sh 'docker build -t 192.168.64.12:5000/worker:latest .'
          sh 'docker push 192.168.64.12:5000/worker:latest'
        }
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        sh 'kubectl apply -k k8s/overlays/dev'
      }
    }
  }
}