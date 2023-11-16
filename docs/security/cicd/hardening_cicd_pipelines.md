# Hardening CICD Pipelines

| Revision | Change | Date | Author | Approver |
| --- | --- | --- | --- | --- |
| 0.1 | Initial Release | 25 Sept 2023 | Shoaib S. | Shoaib S. |

---

## 1. Configuring branch protection rules, artifact validation, and approvals

Configure branch protection rules to enforce security requirements, such as only allowing signed commits and merging only reviewed code to the branches that trigger production deployment.

Another important practice is to have an approval-based system that requires all code changes to be reviewed and validated before they can be merged and trigger deployment. This adds an additional layer of security to the system and ensures that no single entity(human/machine) can push code to production. This helps in resolving the risks of insufficient flow control mechanisms ([CICD-SEC-1](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-01-Insufficient-Flow-Control-Mechanisms))

Allow only signed and validated artifacts to flow through the CI/CD pipeline. This ensures that only trusted and legitimate artifacts are deployed to production, thereby minimizing the risk of security breaches. To implement this, it is recommended to use a rigorous validation process that scrutinizes each artifact before it moves further down the pipeline and helps in preventing improper artifact integrity validation ([CICD-SEC-9](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-09-Improper-Artifact-Integrity-Validation)).

With these measures in place, the CI/CD pipeline can operate securely and efficiently.

## 2. Access control based on the principle of least privilege
Access control is a fundamental aspect of any secure system. The principle of least privilege (PoLP) is a guiding principle in access control that limits users and machines to only the permissions necessary for their respective tasks. By implementing the PoLP, you can reduce the risk of security breaches that could arise from users with excessive privileges.

It is essential to maintain clear visibility of who has access to what in order to maintain proper access control. This visibility ensures that the privileges assigned to each user or machine are limited to their scope of work. Additionally, regular audits and reviews of access control mechanisms can help identify and correct any potential misconfigurations or weaknesses that may exist.

## 3. Having security and quality gates
Security and quality gates serve as checkpoints in the CI/CD pipeline that detect potential issues, vulnerabilities, or other problems early on. These gates can prevent malicious code from being deployed to production and ensure that only code and artifacts that meet the required security and quality standards move further down the pipeline.

## 4. Enforce secure coding standards
Enforcing secure coding standards can help in preventing known vulnerabilities in code at the time of development itself by adhering to a set of secure coding rules and guidelines. A good place to start is [OWASP secure coding practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/).

## 5. Keep credentials safe
One of the most important aspects of securing CI/CD pipelines is to keep credentials safe. CI/CD pipelines are a gold mine of sensitive secrets and credentials such as access keys, API tokens, and login credentials. These should never be hardcoded or stored in plain text. Instead, they should be encrypted and stored in a secure location with access only given to the scope in which they are needed. Furthermore, just-in-time access should be enabled wherever possible to reduce the exposure of secrets.

## 6. Clean up temporary resources
CI/CD pipelines are dynamic in nature, which means that temporary resources are frequently created, and these resources can pose a significant security risk.

Nodes perform multiple jobs in the CI/CD pipeline, and these jobs often require temporary resources such as containers and artifacts. If these resources are not properly cleaned up after use, they can linger on the node and create potential security vulnerabilities.

Cleaning up these temporary resources is, therefore, a critical part of hardening CI/CD pipelines. This process involves removing any artifacts, containers, or other resources that were created during the pipeline execution. By doing so, the risk of an attacker gaining access to sensitive data or exploiting vulnerabilities is significantly reduced.

## 7. Automation of security tasks
Automation is the key to improving security by eliminating human errors. Automate routine security tasks, such as scanning for vulnerabilities or applying security patches. This also helps the security team to focus on more complex tasks and allows them to respond more quickly to security incidents.

## 8. Configure local security plugins, linters, and pre-commit hooks
Shifting security left means implementing security measures that can detect issues at the earliest. Equipping the developer engineering environment with tools like security plugins, linters, etc can detect any security issues at the time of writing the code itself and avoid running this vulnerable code in CI/CD pipelines.

Additionally, pre-commit hooks can be configured with a set of security rules to detect any security issues at the time of committing.

Some examples of such plugins and tools are [TFLint](https://spacelift.io/blog/what-is-tflint), [snyk plugin for intellij](https://snyk.io/blog/secure-coding-with-jetbrains-ide-plugin/), [pre-commit](https://pre-commit.com/), etc.

## 9. Misconfiguration detection
Detecting misconfigurations in the CI/CD process is crucial in ensuring the security and integrity of the system. Regular scanning and monitoring of all systems involved can help identify potential security issues or misconfigurations that may be exploited by an attacker. These misconfigurations can involve network settings, access control policies, and infrastructure security configurations.

It’s important to keep all nodes updated and patched regularly to prevent known vulnerabilities from being exploited. By proactively identifying and addressing misconfigurations, the security posture of the CI/CD pipeline can be strengthened and better protected against attacks and helps in resolving one of the common risks of insecure system configuration ([CICD-SEC-7](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-07-Insecure-System-Configuration)).

## 10. Have a response plan
It is crucial to acknowledge that despite implementing all the necessary security measures, no system can be considered completely secure. Therefore, it is necessary to have a well-defined response plan in case of any security breach or system failure. Such a plan should aim to mitigate and control the damage caused and recover from the incident as quickly as possible.

Having a set of incident response Standard Operating Procedures (SOPs) is vital in dealing with such situations. These procedures should outline the steps to be taken in case of a breach or system failure depending on the nature of the incident. For example, temporary revocation of admin-level access.

Aside from the best practices mentioned above, keep security in mind when picking your CI/CD platform. For example, security is one of [Spacelift’s](https://spacelift.io/) biggest priorities, and apart from the state-of-the-art [security solutions](https://docs.spacelift.io/product/security.html) that are embedded inside the product like [Policy as Code](https://docs.spacelift.io/concepts/policy/index.html), Encryption, [Single Sign On (SSO)](https://docs.spacelift.io/integrations/single-sign-on/index.html), [Private Worker Pools](https://docs.spacelift.io/concepts/worker-pools), and others. In some organizations, there are tools that engineers were accustomed to and want to have the possibility to integrate them. When it comes to integrating security tools in your workflows, Spacelift has you covered with the Custom Inputs feature. Read more on [integrating security tools with Spacelift](https://spacelift.io/blog/integrating-security-tools-with-spacelift).

Spacelift also adds an extra [layer](https://docs.spacelift.io/concepts/policy/) of policy that allows you to control – separately from your infrastructure project – [what changes can be made](https://docs.spacelift.io/concepts/policy/terraform-plan-policy), [when, and by whom](https://docs.spacelift.io/concepts/policy/stack-access-policy). This isn’t only useful to protect yourself from the baddies but allows you to implement an [automated code review pipeline](https://docs.spacelift.io/concepts/policy/terraform-plan-policy#automated-code-review)
