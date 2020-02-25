#!/bin/bash

ssh interview@54.165.65.69 "git clone https://github.com/riptidewave93/test-app.git -b improvements /home/interview/test-app && cd /home/interview/test-app/ && ./setup.sh && ./deploy-server.sh"
