# Managing Provider Configuration

| Revision | Change          | Date         | Author   | Approver  |
| ---      | ---             | ---          | ---      | ---       |
| 0.1      | Initial Release | 25 Sept 2023 | Alkaif   |  |

## Objectives

Managing Provider Configuration

## Problem Statement

The challenge is to efficiently manage and standardize provider configuration settings in Terraform across multiple environments. 


Providers are Terraform plugins that are used to interact with remote systems such as Docker, AWS, Azure…

## Configuring Single AWS Provider

Every root module will have at least one default provider which then will be used by all the child modules.

By default, resources use a default provider configuration (one without an alias argument).

Configure a single AWS provider in terraform so that we can apply our changes to that particular AWS account.

```
provider "aws" {
  region = "us-east-2"
}
```
## Configuring Multiple AWS providers

Set up multiple AWS providers and use them for creating resources in both AWS accounts.

For each additional non-default configuration, use the alias meta-argument to provide an extra name segment.

```
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "west"
  region = "us-west-2"
}

```

By default, resources use a default provider configuration (one without an alias argument) inferred from the first word of the resource type name.

To use an alternate provider configuration for a resource or data source, set its provider meta-argument to a

```
<PROVIDER NAME>.<ALIAS> 

resource "aws_instance" "foo" {
  provider = aws.west
}


```


