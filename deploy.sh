#!/bin/bash

docker login -u iondodon -p Eronat98

docker pull iondodon/lrmodel:stage-v1.0

docker run -p 5000:5000 lrmodel