#!/bin/bash

ufw allow 5000

docker login -u iondodon -p Eronat98
docker pull iondodon/lrmodel:Rv1.0
docker run --name lrmodel -p 5000:5000 iondodon/lrmodel:Rv1.0