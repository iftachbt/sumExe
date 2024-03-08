pipeline {
  agent any
  stages {
    stage('asd') {
      parallel {
        stage('delete pre image') {
          steps {
            sh '''docker rmi sumimage
'''
          }
        }

        stage('build image') {
          steps {
            sh '''docker build -t sumimage .
'''
          }
        }

      }
    }

    stage('dockerhub') {
      parallel {
        stage('login') {
          steps {
            sh '''docker login -u iftachbt -p dockerhp,j13531
'''
          }
        }

        stage('tag') {
          steps {
            sh 'docker tag sumimage iftachbt/sumimage:latest'
          }
        }

        stage('push') {
          steps {
            sh '''docker push iftachbt/sumimage
'''
          }
        }

      }
    }

    stage('k8s') {
      parallel {
        stage('rm image') {
          steps {
            sh 'docker rmi sumimage'
            sh 'ls'
            sh 'pwd'
          }
        }

        stage('deployment') {
          steps {
            sh '''kubectl apply -f sumexe-deployment.yaml
--validate=false
'''
          }
        }

        stage('service') {
          steps {
            sh '''kubectl apply -f sumexe-service.yaml
--validate=false
'''
          }
        }

      }
    }

    stage('test') {
      steps {
        sh 'kubctl get pods'
      }
    }

  }
}