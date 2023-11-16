# Securing CICD Pipelines

| Revision | Change | Date | Author | Approver |
| --- | --- | --- | --- | --- |
| 0.1 | Initial Release | 25 Sept 2023 | Shoaib S. | Shoaib S. |

---

## Objective

The goal here is to understand what are the areas that can be compromised and explain some strategies to overcome those.

## Challenge

The engineering ecosystem we usually have:

![security](__assets__/Screenshot%202023-10-01%20at%2010.53.17%20PM.png)

As depicted in above diagram, ideally we have the following in our CICD pipelines:

- Multiple stages (Version Control Checkout, Build, Test, Deploy)
- Version Control Repositories that host the application code.
- 3rd party tools like Sonarqube, Notification Tools, etc.
- Collaborators (People, Automation Tools, Services, etc)
- And lots of PAT Tokens, Keys, Secrets, etc for these integrations to work.

But, as we grow the above eco-system turns to something like this ugly mess

![mess](__assets__/Screenshot%202023-10-01%20at%2010.55.11%20PM.png)

This raises lots of security concerns as follows:

- How do you enforce Least Privilege Policy?
- How do you know your token expired?
- How do you know that your CI or CD is not compromised?
- How do you know that your Server itself is compromised?
- and more like these…

![complex-interaction](__assets__/Screenshot%202023-10-01%20at%2010.59.00%20PM.png)

Above image shows the complex interactions of these components with each other.

## Pipeline Security Strategies

SIP (Security in Pipeline)
SOP (Security of Pipeline)
SAP (Security Around Pipeline)

![sip-sap-sop](__assets__/Screenshot%202023-10-02%20at%2010.43.25%20AM.png)

### SIP

![sip](__assets__/Screenshot%202023-10-02%20at%2012.19.30%20AM.png)

Above image represents how to add security in the pipeline applications and codes.

Security in the Pipeline means, securing your application code, scanning for vulnerabilities, performing code coverage tests.

Following table suggests some tools to use:

| Source Code Language | Security Tools |
| --- | --- |
| All | SonarQube |
| NodeJS | nodejsscan |
| Terraform | Checkov |
| Docker | Snyk |

Below image show report showing severity of repos.

![issue](__assets__/Screenshot%202023-10-02%20at%2012.19.45%20AM.png)

### SOP

![sop](__assets__/Screenshot%202023-10-02%20at%2012.20.46%20AM.png)

SOP suggests that as we have various systems in place for securing the perimeter breach, abuse of cloud misconfigurations and exploiting development endpoints, we should also consider CICD as a new gateway for hackers to reach out to your production systems.

SOP includes:

- Using Least Privilege Access Policy
- Using Cloud or Secure Open source solutions for storing your pipeline secrets.
- Provide Least needed access TO the pipeline (Users accessing pipelines)
- Provide Least needed access BY the pipeline (Pipeline accessing resources)

### SAP

![sap](__assets__/Screenshot%202023-10-02%20at%2012.21.21%20AM.png)

SAP suggests that:

- Make sure nothing can bypass the pipeline and push something to artifact stores or production environments.
- Power to release to production should only be given to the Pipeline and from no where else, this helps reduce the attack surface and you will know that the pipeline is the only entrypoint to production systems.


## Case Studies

Below table shows the CICD security breaches on these companies and the losses they incurred due to that along with a link to the same.


| Compromised Product/Company | Description |
| --- | --- |
| Solarwinds | Security incident, where attackers targeted the pipeline, affecting more than 18,000 organizations and gaining access to their networks, systems, and data undetected for over 14 months. |
| Codecov | Codecov’s had their environments breached by attackers. Clients that used Codecov’s products in their CICD pipelines had their Secret Keys and Tokens, exfilterated to the Attackers Cloud. |
| PHP | The main code repository for PHP, which powers nearly 80 per cent of the internet, was breached to add malicious code |
| StackOverflow | Vulnerabilities in the build systems led to stolen source code and leaked secrets. An unauthorised person had logged into its development system and escalated their access to the production version of stackoverflow.com. The source code for the site as well as the names, IP addresses and email addresses of 184 users was stolen, but not the databases which contain the content of the site and that of its customers. |

## Why is CI/CD Security Crucial?
The CI/CD pipeline is the backbone of software development organizations, enabling them to build, test, and deliver any software faster, more frequently, and more reliably.

But what happens when these pipelines break?
This can result in significant chaos, hampered collaboration, and delays in delivering new code to end-users, leading to a loss of revenue, reputation, and even legal consequences.
If this gives you goosebumps, there is something even scarier.

What happens if these pipelines are compromised by attackers? Worse yet, what if this occurs and the security incident is not detected for a long time or at all?” 😲

Consider the SolarWinds CI/CD security incident, where attackers targeted the pipeline, affecting more than 18,000 organizations and gaining access to their networks, systems, and data undetected for over 14 months. This attack alone underscores the critical need for CI/CD security, and it’s not the only one. The StackOverflow incident, where vulnerabilities in the build systems led to stolen source code and leaked secrets, the php backdoor attack, and the CodeCov exploit all serve as examples of the devastating effects of CI/CD security breaches.

The significance of protecting the CI/CD process cannot be overstated, and it has shifted the focus of security teams in recent years.

## What is CI/CD Security?
CI/CD security refers to the practice of integrating security into the CI/CD pipeline to identify and remediate any risks or vulnerabilities throughout all the stages of the CI/CD process. To protect your pipeline against potential threats, it is essential to understand the top security risks associated with CI/CD pipelines.

## Security Measures

There are several measures we can undertake to build a secure CI/CD pipeline. Some of them are as follows:

### 1. Integrating Source Composition Analysis (SCA)
One of the most critical steps in securing a CI/CD pipeline is integrating SCA tools. SCA is an AppSec methodology that analyzes all open-source components and dependencies in a project to detect any vulnerabilities, issues, or risks. It can help in mitigating dependency chain abuse ([CICD-SEC-3](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-03-Dependency-Chain-Abuse)), like dependency hijacking, dependency confusion, etc.

SCA tools can be easily integrated with popular CI/CD providers and source control to automatically scan and detect security issues and vulnerabilities.

Some of the most popular SCA providers in the market are Snyk, JFrog Xray, and GitLab.

### 2. Integrating Static Application Security Testing (SAST)
Static application security testing (SAST) is an AppSec methodology that scans project source code, byte code, and binaries to detect any issues or vulnerabilities like SQL injection, broken access control, insecure design, etc. 

SAST goes hand in hand with SCA and helps in detecting and mitigating [OWASP top 10](https://github.com/OWASP/API-Security/tree/master/2023/en/src) and other vulnerabilities in the source code. By integrating SAST, you can identify vulnerabilities early in the development cycle and save time and resources.

Some of the most popular SAST providers in the market are Checkmarx, Fortify, Sempgrep, Snyk, and SonarQube.

### 3. Access control
As we saw earlier, inadequate identity and access management ([CICD-SEC-2](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-02-Inadequate-Identity-And-Access-Management)) and insufficient pipeline-based access control ([CICD-SEC-5](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-05-Insufficient-PBAC)) are two of the top risks for CI/CD.

To address these, it is important to ask 2 questions in the context of access control for the CI/CD pipelines:

- Who has access to the pipelines, and the limit of their access?
- What access do the pipelines have to do their job?
  
#### Managing access to the pipelines
Pipelines are at the heart of developing, testing and distributing software, and many identities require access to them. More often than not, these identities are overly permissive, shared, and sometimes even stale (not in use). This may create an opportunity for an attacker to gain access to the pipelines, aka the crown jewels of your organization.

It is, therefore, important to manage them well and grant access based on the principle of least privilege. Moreover, identities should not be shared and regularly audited to clean up any stale identities to mitigate all risks associated with them.

#### Managing access of the pipelines
CI/CD pipelines are high-value resources, often requiring a high level of access to multiple sensitive resources to do their job. Sometimes, pipelines are granted all the permissions, which poses a severe risk. If an attacker gains access to an overly privileged pipeline, she can exploit this to move laterally in the engineering ecosystem and can do significant damage.

It is important to limit the access of the pipelines to only the necessary permissions to avoid any lateral movement in case they are compromised. Moreover, no pipelines should share the same set of permissions or nodes that they run on unless their job functions are identical.

### 4. Threat modeling
Threat modeling is a proactive approach that helps to identify potential risks and threats to the CI/CD pipeline. This process involves analyzing the system and identifying potential vulnerabilities and weaknesses that could be exploited by attackers.

Once these threats are identified, appropriate countermeasures can be implemented to prevent or mitigate them, thereby improving the overall security posture of the system. By regularly conducting threat modeling exercises, organizations can ensure that their CI/CD pipelines remain secure and resilient against potential attacks.

### 5. Secure secrets management
The management of secrets and credentials is a critical aspect of securing a CI/CD pipeline and can help prevent insufficient credential hygiene ([CICD-SEC-6](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-06-Insufficient-Credential-Hygiene)).

Avoid hardcoding secrets and ensure that they are not checked into source code. IDE security plugins, pre-commit hooks, and regular repository scans can help detect hard-coded secrets and protect against inadvertently logging sensitive information. 

Secrets should be stored in an encrypted format, and the permissions associated with them should follow the principle of least privilege. It is important not to share them with others (users/machines).

Periodically rotate all static secrets and remove outdated ones. Additionally, logging and monitoring can aid in detecting and mitigating the unauthorized use of secrets and other potential threats.
Tools like HashiCorp Vault, AWS Secrets Manager, Knox, etc, can be used to effectively manage secrets and reduce the risk of a security breach.

### 6. Securing containers and registry
As the use of containers in software development and delivery continues to grow, securing them becomes more critical. Attackers can exploit vulnerabilities in container images or insecure networking and even gain root privileges on the host to compromise CI/CD pipelines.

One way to mitigate the risks associated with containers is to regularly scan images and registries to detect any potential security issues or vulnerabilities and remediate or mitigate them.

Tools such as Aqua Security, Qualys, etc., help to detect and mitigate any security issues around container images or registries.

Read more about [Container Security Best Practices](https://spacelift.io/blog/container-security).

### 7. Protect CI/CD configurations
The CI/CD configurations are frequently saved alongside the code. GitHub workflow configurations, for example, are frequently stored in the same repository under the path .github/workflows. Anyone with repository access can easily modify these configurations and manipulate the CI/CD process.

Branch protection rules are therefore required for branches that are configured to trigger a pipeline in the CI/CD system, and any configuration changes must be reviewed before running. Alternatively, these configurations can be managed in a branch separate from the one used for pushing code. The branch that contains the configuration should be marked as protected.

These measures can help in protecting against poisoned pipeline execution ([CICD-SEC-4](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-04-Poisoned-Pipeline-Execution)).

### 8. Dependency management
Dependency management can help against dependency chain abuse ([CICD-SEC-3](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-03-Dependency-Chain-Abuse)). All packages should be pulled from an internal registry that only contains pre-vetted packages instead of directly pulling them from the internet.
Checksum and signature verification should be enabled to ensure that clients receive the correct dependencies. Additionally, lock the package version and avoid pulling the most recent versions without first ensuring that the most recent version is free of vulnerabilities.


### 9. Logging, monitoring, observability, and alerts
Lack of visibility can lead to an attack going unnoticed and make it challenging to investigate an incident and determine the extent of the breach.

Effective logging, monitoring, observability, and alerts are crucial for securing a CI/CD pipeline. They help in remediating insufficient logging and visibility ([CICD-SEC-10](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-10-Insufficient-Logging-And-Visibility)) risk.

Logging events such as user/machine access, configuration changes, triggers, and code execution context can aid in incident investigation. Proper monitoring and observability enable the system to be observed and detect any anomalies indicating a security incident or vulnerability.

Alerts complement logging and monitoring by bringing the detected anomalies to the surface in near real-time. Tools like ELK and [Prometheus-Grafana](https://spacelift.io/blog/prometheus-kubernetes) can be used for effective monitoring and observability.

### 10. Auditing
Auditing is an essential part of maintaining a secure CI/CD pipeline. Regular audits ensure that the systems and processes within the pipeline are compliant with the security standards and policies established by the organization. These audits can identify any weaknesses or vulnerabilities in the system that could be exploited by an attacker and assess whether the security measures in place are effective in protecting the system.

Access control auditing is particularly important in the context of CI/CD pipelines. This involves verifying that the right people have access to the right resources and that they only have the level of access they need to perform their job functions.

Regularly auditing 3rd party integrations help in mitigating ungoverned usage of 3rd party services ([CICD-SEC-8](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-08-Ungoverned-Usage-of-3rd-Party-Services)), as these integrations often have access to sensitive information and resources, and any vulnerabilities in these integrations can be exploited to compromise the entire pipeline.

All these measures help in securing your CI/CD pipeline. In the [next](hardening_cicd_pipelines.md) section, we will discuss some best practices to keep in mind for hardening CI/CD pipelines.
