#!/bin/bash

docker build -t app:v1 .
docker run -p 5000:80 app:v1
