#!/bin/bash
docker stop s21a313
docker rm s21a313
docker rmi s21_alpine_3.13
docker build --no-cache -t s21_alpine_3.13 .
docker run --rm --name s21a313 -di s21_alpine_3.13
# docker exec -it s21a313 sh
# docker stop s21a313
