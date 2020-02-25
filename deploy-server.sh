#!/bin/bash

docker build -t app:v1 .
docker run -p 80:5000 -d app:v1
