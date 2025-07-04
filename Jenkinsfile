pipeline {
  agent any

  stages {
    stage('Build Producer') {
      steps {
        dir('image-worker/producer') {
          sh 'docker build -t registry.ci-vm:5000/producer:latest .'
          sh 'docker push registry.ci-vm:5000/producer:latest'
        }
      }
    }

    stage('Build Worker') {
      steps {
        dir('image-worker/worker') {
          sh 'docker build -t registry.ci-vm:5000/worker:latest .'
          sh 'docker push registry.ci-vm:5000/worker:latest'
        }
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        sh 'kubectl apply -k image-worker/k8s/overlays/dev'
      }
    }
  }
}