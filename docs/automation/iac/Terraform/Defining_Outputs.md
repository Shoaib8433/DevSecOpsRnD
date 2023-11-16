# Defining Outputs

| Revision | Change          | Date         | Author   | Approver  |
| ---      | ---             | ---          | ---      | ---       |
| 0.1      | Initial Release | 25 Sept 2023 | Alkaif   |           |

## Objectives 

To provide a clear and structured way to expose important information and data generated during the Terraform provisioning process, making it accessible for reference, monitoring, and integration with other systems.

## Solution

Terraform will store hundreds or even thousands of attribute values for all the defined resources in our infrastructure in a state file.

An output attribute can not only be used for the user reference but it can also act as an input to other resources being created via Terraform.

### Terraform example code for output value 
### aws_instance public_dns

```

provider "aws" {
  region     = "us-east-1"
  access_key = "AKIAQ3MZANMSAGUBLIPNMN"
  secret_key = "cCALzrQG7RMII7GosylEC70di3D1NBbAOEGAsWhgm"
}

resource "aws_instance" "web" {
  ami           = "ami-08f3d892de259504d"
  instance_type = "t2.micro"
  tags = {
      Name = "Prod_instance"
  }
  }

# Let's define an output to show public DNS address 

output "address" { 

value = aws_instance.web.public_dns

 }

```
## Refrences 

[developer.hashicorp.com](https://developer.hashicorp.com/terraform/tutorials/configuration-language/outputs)

[Terraform Output Values : Complete Guide & Examples](https://devpress.csdn.net/cicd/62ec861089d9027116a1127e.html)

