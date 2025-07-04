pipeline {
  agent any

  stages {
    stage('Build Producer') {
      steps {
        dir('producer') {
          sh 'docker build -t registry.ci-vm:5000/producer:latest .'
          sh 'docker push registry.ci-vm:5000/producer:latest'
        }
      }
    }

    stage('Build Worker') {
      steps {
        dir('worker') {
          sh 'docker build -t registry.ci-vm:5000/worker:latest .'
          sh 'docker push registry.ci-vm:5000/worker:latest'
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