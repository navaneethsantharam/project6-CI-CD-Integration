# Overview

The project actually does the prediction on Boston housing data set. More details about dataset are available @ https://www.kaggle.com/c/boston-housing
A flask application has been built with an endpoint /predict. The endpoint takes the input paramaters and predicts the median value of owner-occupied homes.

## Project Plan
Project Plan

* A link to a Trello board for the project @ https://trello.com/b/59QIvgTv/ci-cd-project-6-plan
* A link to a spreadsheet that includes the original and final project plan @ [project-management-template.xlsx](https://github.com/navaneethsantharam/flask-ml-service-with-azuredevops/files/9641407/project-management-template.xlsx)

## Instructions

* Architectural Diagram (Shows how key parts of the system work)>
![flask_app_architecture](https://user-images.githubusercontent.com/108083391/192158289-25455529-6ac5-4cac-9b88-d28752b638de.jpg)


Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service
![7_Creating_app_service_and_deploying_flask](https://user-images.githubusercontent.com/108083391/192241707-f25ea326-393a-42a4-9dd7-3c04e42536b6.jpg)


* Project cloned into Azure Cloud Shell
![1_git_clone](https://user-images.githubusercontent.com/108083391/192231828-715571c7-5400-405f-bdec-d33e2c371f44.jpg)


* Passing tests that are displayed after running the `make all` command from the `Makefile`
![2_make_all](https://user-images.githubusercontent.com/108083391/192231926-70cdcd5b-cf50-43df-9ce6-4108b630e669.jpg)
![2_make_all_2](https://user-images.githubusercontent.com/108083391/192231951-7cc9aa21-8885-49d7-8f61-48c0ea8ca07c.jpg)


* Enabling git actions and testing for build success on commit
![3_git_action_build](https://user-images.githubusercontent.com/108083391/192235456-10606ba1-ffe7-4da1-916c-9e2e0164ed7a.jpg)


* Status badge for git actions


[![Python application test with Github Actions](https://github.com/navaneethsantharam/project6-CI-CD-Integration/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/navaneethsantharam/project6-CI-CD-Integration/actions/workflows/pythonapp.yml)


* Running flask application locally
![4_Local_flask_run](https://user-images.githubusercontent.com/108083391/192236472-c55a82fc-ed27-4241-8d96-a06da3a6eb9f.jpg)


* Output of a test run
![5_local_flask_output](https://user-images.githubusercontent.com/108083391/192236493-77973093-ad0d-4c96-83d2-95450e1f5d5f.jpg)


* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).
![12_Build_Success](https://user-images.githubusercontent.com/108083391/192246469-13a218e0-c3b9-4ca6-9ecc-7eff6eb010de.jpg)
![13_Deploy_Success](https://user-images.githubusercontent.com/108083391/192246811-9095de20-854d-4a0e-8fb8-3a5cf7b78ed5.jpg)


* Running Azure App Service from Azure Pipelines automatic deployment
![14_Azure_pipeline_Success](https://user-images.githubusercontent.com/108083391/192246922-92ac3c05-02fe-45bf-a414-dfec2715d514.jpg)


* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:
```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```
![8_Test the app service output prediction](https://user-images.githubusercontent.com/108083391/192241636-3b238f59-db62-47cd-9141-405653609df4.jpg)


* Output of streamed log files from deployed application
![11_log_stream](https://user-images.githubusercontent.com/108083391/192245109-d57dc975-76c1-44e9-a1a7-339dfc65363f.jpg)


* Load testing done using Locust. Locust.py has the code to invoke the test scenario for API performance

Command used-
"locust -f locust.py --host https://flask-ml-service.azurewebsites.net:443 --autostart --users 50 --spawn-rate 5 --run-time 30 --autoquit 5"
![10_Locust_test](https://user-images.githubusercontent.com/108083391/192244695-d0bed286-a7e0-4c0c-9cf3-54e1726db61e.jpg)


## Enhancements

1.Endpoint can be created to do bulk predictions.

2.Apply autoscaling(in app service) for the flask application based on the number of user requests.


## Demo 

Youtube link for demo available@ https://youtu.be/0TBg7kQZ-6c

