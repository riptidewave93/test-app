#!/bin/bash

docker build -t app:v1 .
docker stop app; docker rm app;
docker run -p 80:5000 --name app -d app:v1
