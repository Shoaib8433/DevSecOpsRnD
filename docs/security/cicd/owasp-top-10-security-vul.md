# OWASP Top 10 CI/CD Security Risks

| Revision | Change | Date | Author | Approver |
| --- | --- | --- | --- | --- |
| 0.1 | Initial Release | 25 Sept 2023 | Shoaib S. | Shoaib S. |

---

## [CICD-SEC-1](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-01-Insufficient-Flow-Control-Mechanisms): Insufficient Flow Control Mechanisms

The first CI/CD security risk on the list refers to the ability of an attacker who has gained access to any of the systems in the CI/CD process (SCM, CI, or runners) to push malicious code down the pipeline due to a lack of control mechanisms that enforce additional approval or review.

### Why is this bad?
CI/CD pipelines are a direct bridge from the developers’ machine to the production environment. In the absence of flow control like reviews or approvals, a single entity (human or machine) can push malicious code to production and publish packages with malicious code.

This means that once the system is compromised, there are no constraints to the limit of the damage that the malicious actors can do.

### How was this exploited?
- An attacker planted a backdoor in the [PHP](https://news-web.php.net/php.internals/113981) git repository by pushing malicious unreviewed code.
- On Homebrew, a security researcher found a way to [abuse](https://brew.sh/2021/04/21/security-incident-disclosure/) the auto-merge rules to push malicious code.

## [CICD-SEC-2](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-02-Inadequate-Identity-And-Access-Management): Inadequate Identity and Access Management

This refers to the lack of proper identity and access management in CI/CD ecosystems, given the vast number of identities to manage and the complexity of interconnected systems involved, such as SCM and CI, which often have different authentication and authorization methods.

In many cases, user/machine accounts do not follow the principle of least privilege and have overly permissive default permissions.

### Why is this bad?
The consequences of inadequate identity and access management in CI/CD processes are severe. The existence of multiple identities paired with poor identity and access control creates an opportunity for hackers, where compromising a single account could lead to them having control over the systems involved in the CI/CD process. In the worst case, it can even serve as a path to reach production, leading to devastating consequences for the organization.

### How was this exploited?
Several instances show how this risk has been exploited in the past. For instance:
- [StackOverflow](https://stackoverflow.blog/2021/01/25/a-deeper-dive-into-our-may-2019-security-incident/) team city CI server was compromised, where the attacker was able to escalate their privilege in the environment, as newly registered accounts were granted admin privileges by default.
- A self-managed [GitLab](https://techcrunch.com/2021/06/24/an-internal-code-repo-used-by-new-york-states-it-office-was-exposed-online/) server of the New York state government having sensitive secrets was compromised as it allowed anyone to self-register and get access.

## [CICD-SEC-3](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-03-Dependency-Chain-Abuse): Dependency Chain Abuse

When it comes to the security of a CI/CD pipeline, one of the biggest risks is dependency chain abuse. It happens when hackers exploit the way in which dependencies are pulled, enabling them to fetch and execute malicious packages.

### Why is this bad?
Once downloaded, the package can run itself and perform a variety of nefarious actions, such as stealing sensitive data, compromising credentials, or even sneaking into the production environment.

There are several attack vectors, including [dependency confusion](https://dhiyaneshgeek.github.io/web/security/2021/09/04/dependency-confusion/), [dependency hijacking](https://cyware.com/news/analyzing-the-deadly-rise-in-npm-package-hijacking-78b24364), [typosquatting](https://snyk.io/blog/typosquatting-attacks/), [brandjacking](https://blog.sonatype.com/twilio-npm-is-brandjacking-malware-in-disguise).

### How was this exploited?
Several notable incidents demonstrate the threat of dependency chain abuse.
- The popular ua-parser-js NPM library, with 9 million downloads a week, was [hijacked](https://github.com/advisories/GHSA-pjwm-rvh2-c87w) to launch crypto-miners and steal credentials.
- Amazon, Zillow, Lyft, and Slack NodeJS apps [targeted](https://www.bleepingcomputer.com/news/security/malicious-npm-packages-target-amazon-slack-with-new-dependency-attacks/) using the dependency confusion vulnerability.

## [CICD-SEC-4](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-04-Poisoned-Pipeline-Execution): Poisoned Pipeline Execution (PPE)

Poisoned Pipeline Execution (PPE) is a threat to CI/CD pipeline security and refers to the ability of a hacker who has access to the SCM without having direct access to CI/CD pipelines to manipulate the build process by modifying/poisoning the CI configuration files to run malicious commands.

### Why is this bad?
The consequences of PPE can be severe, as CI environments are often a central source of sensitive secrets, credentials tokens, and more. The attacker can poison the CI process with malicious commands to compromise and send sensitive secrets like cloud provider credentials, artifact repository credentials, etc, to remote servers by modifying the build process in the CI pipeline.

Build and deploy steps can also be modified to directly promote malicious builds to production.

### How was it exploited?
- GitHub Actions were [abused](https://dev.to/thibaultduponchelle/the-github-action-mining-attack-through-pull-request-2lmc) to mine cryptocurrency by pull requests that contained malicious code.
- [Abusing](https://alex.kaskaso.li/post/terraform-plan-rce) the [terraform plan command](https://spacelift.io/blog/terraform-plan) for execution of OS commands in the CI/CD, by [Alex Kaskasoli](https://twitter.com/alxk7i).

## [CICD-SEC-5](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-05-Insufficient-PBAC): Insufficient PBAC (Pipeline-Based Access Controls)

PBAC refers to access controls that are implemented at the pipeline level. These controls determine what resources the pipeline can access and what actions it can perform. Insufficient PBAC means that the access controls are not granular enough, allowing a pipeline stage to have more permissions than it requires.

### Why is this bad?
Malicious code that gains access to a pipeline stage can access the same resources and systems as that stage. An overly permissive stage can be used by an attacker to get access to secrets and/or connect to any resources the pipeline has access to. An attacker who gains access to the pipeline can exploit these permissions to move laterally inside and outside the execution environment, accessing sensitive systems and exfiltrating secrets.

### How was this exploited?
Recent attacks have highlighted the importance of implementing strong PBAC controls.
- [Codecov](https://about.codecov.io/security-update/) was compromised to steal environment variables.
- A [vulnerability](https://goteleport.com/blog/hack-via-pull-request/) found in Teleport’s CI implementation allowed attackers to run a privileged container and escalate to root privilege — leading to secret exfiltration, the release of malicious artifacts, and access to sensitive systems.


## [CICD-SEC-6](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-06-Insufficient-Credential-Hygiene): Insufficient Credential Hygiene
Insufficient credential hygiene refers to the failure to manage and protect secrets and credentials used in the pipeline due to flaws in access control and over-permissive credentials.

### Why is this bad?
Credentials are among the most valuable data that attackers seek, and a leak can give them access to high-value resources, enabling them to modify the build process or push malicious code to production.

### How was this exploited?
The recent security breaches at Codecov and Samsung serve as a stark reminder of the importance of proper credential hygiene in CI/CD pipelines.

- Codecov was [compromised](https://about.codecov.io/security-update/) by attackers, and thousands of credentials were stolen.
Samsung [spilled](https://techcrunch.com/2019/05/08/samsung-source-code-leak/) SmartThings app source code and secret keys.

## [CICD-SEC-7](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-07-Insecure-System-Configuration): Insecure System Configuration
Security configurations and hardening refer to the process of configuring systems to minimize vulnerabilities and make them less susceptible to attack. In the case of the CI/CD pipeline, this involves implementing proper access controls, minimizing network exposure, and regularly patching and updating systems. Unfortunately, this is often overlooked, making it one of the easiest targets for attackers.

### Why is this bad?
Attackers can exploit the lack of security configurations and hardening to gain unauthorized access to the pipeline, allowing them to move laterally within these systems. This can result in the attacker obtaining sensitive secrets, compromising the build process, or even gaining access to sensitive resources inside and outside the engineering ecosystem. Such unauthorized access can have devastating consequences, not just for the software development process but also for the organization as a whole.

### How was this exploited?
In recent years, several high-profile incidents have highlighted the dangers of poor security configurations and hardening.
- Mercedes-Benz onboard logic unit (OLU) source code was [leaked](https://www.zdnet.com/article/mercedes-benz-onboard-logic-unit-olu-source-code-leaks-online/) as a result of opening a self-maintained Gitlab server for self-registration.
Nissan source code was [leaked](https://www.zdnet.com/article/nissan-source-code-leaked-online-after-git-repo-misconfiguration/) online after Git repo misconfiguration.

## [CICD-SEC-8](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-08-Ungoverned-Usage-of-3rd-Party-Services): Ungoverned Usage of 3rd Party Services
One of the most common vulnerabilities in CI/CD systems is the ungoverned usage of third-party services. CI/CD systems often rely on multiple third-party services and plugins to perform tasks like code scanning and linting. While these integrations can be incredibly useful, they also present a significant risk as they often grant a high level of permissions for resources in the CI/CD system to third-party services. This can significantly expand the attack surface of the organization.

### Why is this bad?
If a third-party service or plugin is compromised, having overly permissive access can lead to attackers pushing malicious code and compromising the CI/CD or even the production environment.

### How was this exploited?
- Attackers [compromised](https://discuss.deepsource.io/t/security-incident-on-deepsource-s-github-application/131) DeepSource granting them full access to the codebase of all clients of DeepSource.
- The database of the Waydev analytics platform was [compromised](https://changelog.waydev.co/github-and-gitlab-oauth-security-update-dw98s) to steal the Github and Gitlab OAuth tokens of their customers.

## [CICD-SEC-9](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-09-Improper-Artifact-Integrity-Validation): Improper Artifact Integrity Validation
Proper artifact integrity validation is essential to ensure that only trusted code is deployed in the CI/CD pipeline. However, attackers can easily exploit the lack of mechanisms to validate artifacts or code, leading to a host of security vulnerabilities.

### Why is this bad?
A deployable artifact is built from multiple sources, such as 3rd party dependencies and internal artifacts. These create multiple entry points where the artifacts can be tampered with, and without proper validation, an artifact having malicious code can easily slip through.

### How was this exploited?
- The code of the Orion software of SolarWinds was changed in the build system during the build process, which [affected](https://www.cyberark.com/resources/blog/the-anatomy-of-the-solarwinds-attack-chain) more than 18000 organizations.

## [CICD-SEC-10](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-10-Insufficient-Logging-And-Visibility): Insufficient Logging and Visibility
One of the biggest challenges in securing the CI/CD pipeline is the lack of visibility into what is happening. Attackers can take advantage of this by carrying out malicious activities undetected.

### Why is this bad?
Insufficient logging and visibility can make it difficult to identify the attacker’s tactics, techniques, and procedures as part of any post-incident investigation. This makes remediation more challenging, as there may be limited information available to guide the response.

Now that we have understood the most common CI/CD security risks, let’s understand the measures to [mitigate](securing_cicd_pipelines.md) them.
