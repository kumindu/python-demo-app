# python-demo-app
python flask application

This workflow will build and push a new container image to Amazon ECR,
and then will deploy a new task definition to Amazon ECS, when a release is created

## To use this workflow, you will need to complete the following set-up steps:

 1. Create an ECR repository to store your images.
    For example: `aws ecr create-repository --repository-name my-ecr-repo --region us-east-2`.
    Replace the value of `ECR_REPOSITORY` in the workflow below with your repository's name.                                                 Replace the value of `aws-region` in the workflow below with your repository's region.

2. Create an ECS task definition, an ECS cluster, and an ECS service.
    For example, follow the Getting Started guide on the ECS console:
    https://us-east-2.console.aws.amazon.com/ecs/home?region=us-east-2#/firstRun
    Replace the values for `service` and `cluster` in the workflow below with your service and cluster names.

3. Store your ECS task definition as a JSON file in your repository.
    The format should follow the output of `aws ecs register-task-definition --generate-cli-skeleton`.
    Replace the value of `task-definition` in the workflow below with your JSON file's name.
    Replace the value of `container-name` in the workflow below with the name of the container
    in the `containerDefinitions` section of the task definition.

4. Store an IAM user access key in GitHub Actions secrets named `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.
    See the documentation for each action used below for the recommended IAM policies for this IAM user,
    and best practices on handling the access key credentials.
    
## To use this kubernetes, you will need to complete the following set-up steps:

 1.Build docker images.
```
   docker build -t {docker_hub_profile_Name}/pythondemoapp .
   
```
 2.Docker push to docker hub
 
```
   docker login
   docker push {docker_hub_profile_Name}/pythondemoapp 
   
```
  3.Deploy to kubernetes deployment
 
 ```
   kubectl run pythonapp --image={docker_hub_profile_Name}/pythondemoapp:latest --port 8000 --labels="app=pythonapp,tier=backend"
 
 ```
 
  4.To get kubernetes deployment,pods
 
 ```
  kubectl get pods
  kubectl get deployment
  
 ```
 
  5.Create kubernetes service
  
 ```
   kubectl expose deployment pythonapp --type=LoadBalancer --port 80 --target-port 8000
 
 ```
 
  6.To get kubernetes services
 
 ```
  
   kubectl get service
  
 ```
 
  7.To scale deployment in kubernetes
  
 ```
   kubectl scale deployment pythonapp --replicas=2
  
 ```

