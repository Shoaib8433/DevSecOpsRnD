# Jenkins Agent as ECS Tasks using Terraform

| Revision | Change          | Date         | Author   | Approver  |
| ---      | ---             | ---          | ---      | ---       |
| 0.1      | Initial Release | 25 Sept 2023 | Alkaif   |  |

## Objectives

-  Optimize resource utilization by running Jenkins agents as containers within the ECS cluster.

- Ensure that Jenkins agent tasks are isolated, well-configured, and secure within the ECS environment.

- Auto-Registration: Implement automatic registration of Jenkins agents with the Jenkins master upon task startup.

- Manage ECS resources efficiently to control infrastructure costs.

- Implement the entire setup using Terraform to enable version-controlled, repeatable infrastructure provisioning.

## Challenge

Our organization has a Jenkins-based Continuous Integration/Continuous Deployment (CI/CD) pipeline for automating software builds and deployments. We have a growing number of CI/CD jobs, and the demand for build and deployment resources varies throughout the day.

## Problem Statement

When setting up a Jenkins build server on a physical machine, right-sizing can become a challenging task. Long idle times followed by high, irregular loads make it hard to predict the necessary hardware requirements.

## SOlution

Solution to this problem is the deployment of a containerized Controller/Agent-based Jenkins setup and to offload workloads to dedicated, transient agents.

![](__assets__/JENKINS_AGENT_ARCHI.png)


 ## Advantages 

1.  Accommodates variable workloads and dynamically provision or decommission agents based on demand.

2. Ensures that Jenkins agents operate within isolated containers, reducing interference and maintaining consistent environments.

3. save on infrastructure costs by only running Jenkins agents when necessary and scaling down during idle periods.

4. Leveraging AWS ECS for Jenkins agents allows for seamless integration with other AWS services, enhancing overall DevOps and CI/CD capabilities.


## Disadvantages 

1. Setting up ECS tasks for Jenkins agents can be more complex than traditional agent provisioning methods.

2.  It may require knowledge of AWS ECS and Terraform, which can be challenging for teams new to these technologies.

3. Ensuring proper resource management and configuration for ECS tasks can be time-consuming.

4.  Regular updates and maintenance of ECS task definitions and Terraform configurations are necessary.

5. Running Jenkins agents as ECS tasks may introduce additional network latency compared to running agents directly on the Jenkins master.

## Refrences

[Jenkins-On-ECS ](https://www.tecracer.com/blog/2023/05/serverless-jenkins-on-ecs-fargate-part-1.html)

[Jenkins Agent On ECS](https://www.tecracer.com/blog/2023/05/serverless-jenkins-on-ecs-fargate-part-2.html)

[Terraform Code For ECS Deployment](https://github.com/Eraszz/tecracer-blog-projects/blob/main/serverless-jenkins-on-ecs/vpc.tf)

