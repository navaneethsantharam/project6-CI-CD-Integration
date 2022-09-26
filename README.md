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
![18_Project running on app service](https://user-images.githubusercontent.com/108083391/192157075-e290d503-bef0-4d3d-a21b-d10bc3d6b2bc.jpg)


* Project cloned into Azure Cloud Shell
![19_Git_project_cloned_in_cloud_shell](https://user-images.githubusercontent.com/108083391/192157131-4667f61b-0a7e-47ae-91d0-ef59d14aee7b.jpg)


* Passing tests that are displayed after running the `make all` command from the `Makefile`
![1_make_all_in_cloud_shell](https://user-images.githubusercontent.com/108083391/192156901-cd4e7dd7-c53d-4385-878e-2c58556103ad.jpg)

* Output of a test run
![2_App_running_from_cloudshell](https://user-images.githubusercontent.com/108083391/192156905-a9854d00-3900-4f3d-a74d-c9ed6e0f2eb5.jpg)


* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).
![13_Build Job Success](https://user-images.githubusercontent.com/108083391/192156820-4fbdcd28-e54e-4840-b6d4-9d8ba8918931.jpg)
![14_Deploy Job Success](https://user-images.githubusercontent.com/108083391/192156816-ff33c82d-769e-4599-9f7e-6148639c49d9.jpg)


* Running Azure App Service from Azure Pipelines automatic deployment
![12_Running the Azure Pipeline](https://user-images.githubusercontent.com/108083391/192156808-6f1b6717-5ff4-47f3-91bb-8ee412196bf3.jpg)


* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:
![3_Getting_predictions_from_local](https://user-images.githubusercontent.com/108083391/192156804-d7ffa418-74be-4321-a195-c7b9d364fb34.jpg)

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```
![17_Successfull prediction from app service](https://user-images.githubusercontent.com/108083391/192156792-ac78803f-c5ae-4672-bc0a-d461e46ee6cd.jpg)


* Output of streamed log files from deployed application
![16_Log Stream](https://user-images.githubusercontent.com/108083391/192156987-6963a25d-c607-4e81-9d42-bd806e2a238f.jpg)


*Load testing done using Locust. Locust.py has the code to invoke the test scenario for API performance

Command used-
"locust -f locust.py --host https://flask-ml-service.azurewebsites.net:443 --autostart --users 50 --spawn-rate 5 --run-time 30 --autoquit 5"
![15_Locust_tested_from_cloud_shell](https://user-images.githubusercontent.com/108083391/192157019-6e41f51a-e33b-466d-b249-2c50eeb83559.jpg)

> 

## Enhancements

1.Endpoint can be created to do bulk predictions.

2.Apply autoscaling(in app service) for the flask application based on the number of user requests.


## Demo 

Youtube link for demo available@ https://youtu.be/0TBg7kQZ-6c

