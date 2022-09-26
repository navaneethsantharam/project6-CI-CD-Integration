#!/usr/bin/env bash
echo "Deploying the flask-ml-service"
az webapp up --resource-group Azuredevops -n flask-ml-service --runtime "PYTHON:3.7"
