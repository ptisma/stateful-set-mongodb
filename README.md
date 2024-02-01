# stateful-set-mongodb
Quick tutorial for stateful sets using MongoDB in replica set mode

minikube start --nodes 3
k apply -f k8/sc.yaml
k apply -f k8/svc.yaml
k apply -f k8/ss.yaml




docker build -t ptisma/mongo-mock-writer writer/
docker push ptisma/mongo-mock-writer:latest


writer-reader has to be in same namespace