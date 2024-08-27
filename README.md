# Practical Assessment : Problem Statement 1

# Prerequisites
1.	Install Docker desktop
2.	Clone the git repository.

**Kubernetes Deployment:**

Deploy the services to a local Kubernetes cluster (e.g., Minikube).

STEP 1: Create a local minikube cluster.
                
                minikube start
                minikube status

**NOTE : minikube status command is used to check the status of the created cluster. For e.g:**
                
                $ minikube status
                 minikube
                 type: Control Plane
                 host: Running
                 kubelet: Running
                 apiserver: Running
                 kubeconfig: Configured



STEP 2: Deploy the kubernetes services which are in Deployment folder of the above repository. Follow the below mentioned command:
          
          $ kubectl apply -f ./Deployment/
            deployment.apps/backend-deployment created
            service/backend-service created
            deployment.apps/frontend-deployment created
            service/frontend-service created



**Verification:**

- Ensure the frontend service can successfully communicate with the backend service.
- Click on the Button "Fetch Message"
- Verify that accessing the frontend URL displays the greeting message fetched from the backend.

  Follow the below command to check the communication between frontend and backend.

  **STEP 1**: Execute the below command to get the URL :
          minikube service assesment1-deployment
  ![image](https://github.com/user-attachments/assets/86639e66-9774-401c-9246-778fdd2c54c7)

  **STEP 2**: Check the above output URL in a browser if it displays the backend messege as below:<br>
         <br>![application opening in container](https://github.com/user-attachments/assets/fc0c780c-38c8-4a6d-8b8d-8be1d5de7f6f)


  **STEP 3**: Check if the URL is working.

          $ curl http://127.0.0.1:60931/
            StatusCode        : 200
            StatusDescription : OK
            Content           : <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>QA Assesment </title>
                    </head>
                    <body>



**Automated Testing:**

- Write a simple test script (using a tool of your choice) to verify the integration between the frontend and backend services.
- The test should check that the frontend correctly displays the message returned by the backend.

  **Above is the automation script in the repository. The script is named as :**

             qatestscript.java

  Run the above script in any IDE (e.g. Eclipse)
    -    Import TestNG Libraries

  If the script works without any errors it will display the below output:
             ![testng results](https://github.com/user-attachments/assets/0f1c1d05-f85e-41e3-a728-2575ea267cd5)



# Practical Assessment : Problem Statement 2

**Objective 1. System Health Monitoring Script:**

Develop a script that monitors the health of a Linux system. It should check
CPU usage, memory usage, disk space, and running processes. If any of
these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the
script should send an alert to the console or a log file.

Solution : The file name is **systemHealthscript.py** . To execute the script follow the below steps:
           
           python3 systemHealthscript.py


**Objective 2. Application Health Checker:**

Please write a script that can check the uptime of an application and
determine if it is functioning correctly or not. The script must accurately
assess the application's status by checking HTTP status codes. It should be
able to detect if the application is 'up', meaning it is functioning correctly, or
'down', indicating that it is unavailable or not responding.

Solution : The file name is **applicationCheck.py** . To execute the script follow the below steps:

           python3 applicationCheck.py
