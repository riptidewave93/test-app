#!/bin/bash

docker build -t app:v1 .
docker run -p 80:5000 --name app -d app:v1
