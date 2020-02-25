#!/bin/bash

# Install docker
apt-get update;
apt-get install -y docker-engine git;

# Add our user to docker group
usermod -aG docker interview;
