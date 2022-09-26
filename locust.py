import time
from locust import HttpUser,task,between

class ApiUser(HttpUser):
    wait_time = between(1,10)
    
    @task
    def access_predictions(self):
        self.client.post(url="/predict",json={
   "CHAS":{
      "0":0
   },
   "RM":{
      "0":6.575
   },
   "TAX":{
      "0":296.0
   },
   "PTRATIO":{
      "0":15.3
   },
   "B":{
      "0":396.9
   },
   "LSTAT":{
      "0":4.98
   }
})

