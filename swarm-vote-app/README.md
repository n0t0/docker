#### Init Swarm

$ docker swarm init 


#### Create Backend and Fronend Networks 


docker network create --ingress --driver overlay


#### Create Worker Service 

$ docker service create --name worker --replicas 1 --network frontend --network backend (worker)


#### Create PostgresSQL DB

$ docker service create --name db --network backend -e POSTGRES_PASSWORD=domisol postgres:9.4

#### Create node.js



