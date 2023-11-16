# Conditional Resource Creation

| Revision | Change          | Date         | Author   | Approver  |
| ---      | ---             | ---          | ---      | ---       |
| 0.1      | Initial Release | 25 Sept 2023 | Alkaif   |  |

## Objectives 

The objective is to selectively create or provision resources in Terraform based on specific conditions and criteria, allowing for dynamic infrastructure provisioning and efficient resource management. 

## Solutions

Conditional resource creation in Terraform allows you to create or destroy resources based on certain conditions or inputs. 

 In this example, we'll create an AWS EC2 instance conditionally depending on the value of the create_instance variable. The variable create_instance controls whether the EC2 instance should be created.

 ```
# Create a Terraform variable to control resource creation
variable "create_instance" {
  description = "Set to true to create an EC2 instance, false to skip it."
  type        = bool
  default     = true
}

# AWS provider configuration
provider "aws" {
  region = "us-west-2" # Change to your desired AWS region
}

# Conditional resource creation based on the variable
resource "aws_instance" "example" {
  count         = var.create_instance ? 1 : 0
  ami           = "ami-0c55b159cbfafe1f0" # Change to your desired AMI
  instance_type = "t2.micro"
  subnet_id     = "subnet-ID" # Change to your subnet ID
  key_name      = "your-key-name" # Change to your key name
  # Other EC2 instance configuration
}


 ```
We define a create_instance variable, which is of type bool and defaults to true. This variable controls whether the EC2 instance should be created or skipped.

```
variable "create_instance" {
  description = "Set to true to create an EC2 instance, false to skip it."
  type        = bool
  default     = true
}
```

We configure the AWS provider with the desired region.

```
provider "aws" {
  region = "us-west-2" # Change to your desired AWS region
}
```

The aws_instance resource uses the count argument to conditionally create the EC2 instance. If var.create_instance is true, one instance will be created. If it's false, no instance will be created.

```
resource "aws_instance" "example" {
  count         = var.create_instance ? 1 : 0
  ami           = "ami-0c55b159cbfafe1f0" # Change to your desired AMI
  instance_type = "t2.micro"
  subnet_id     = "subnet-ID" # Change to your subnet ID
  key_name      = "your-key-name" # Change to your key name
  # Other EC2 instance configuration
}
```
You should replace the placeholder values with your specific AMI, subnet ID, and key name.

To apply this configuration, create a .tf file with the above content, and then you can use terraform apply to create or skip the EC2 instance based on the value of the create_instance variable. For example:

To create the instance: terraform apply -var="create_instance=true"
To skip the instance: terraform apply -var="create_instance=false"
This demonstrates how Terraform can conditionally create resources based on the value of a variable, making your infrastructure more flexible and adaptable to different scenarios.

## Refrences

[terraform-real-use-cases-to-solve-95-of-the-conditional-resources-or-blocks-creation](https://levelup.gitconnected.com/terraform-real-use-cases-of-the-conditional-resources-or-blocks-creation-f0bf9b9fbc87)
