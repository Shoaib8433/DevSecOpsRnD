# Dynamic Blocks and For-Each Loops

| Revision | Change          | Date         | Author   | Approver  |
| ---      | ---             | ---          | ---      | ---       |
| 0.1      | Initial Release | 25 Sept 2023 | Alkaif   |  |

## Dynamic Blocks

Terraform provides the dynamic block to create repeatable nested blocks within a resource.

### Dynamic Blocks Example:

In this example, we'll create multiple AWS security group rules using dynamic blocks based on a list of rules. Each rule will be defined in the list with its properties.

```
# Define a list of security group rules
variable "security_group_rules" {
  description = "A list of security group rules."
  type        = list(object({
    type        = string
    from_port   = number
    to_port     = number
    protocol    = string
    cidr_blocks = list(string)
  }))
  default = [
    {
      type        = "ingress"
      from_port   = 22
      to_port     = 22
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    },
    {
      type        = "egress"
      from_port   = 0
      to_port     = 0
      protocol    = "-1"
      cidr_blocks = ["0.0.0.0/0"]
    }
  ]
}

# Create an AWS security group
resource "aws_security_group" "example" {
  name_prefix   = "example-"
  description   = "Example security group"
  vpc_id        = "vpc-ID" # Change to your VPC ID

  dynamic "ingress" {
    for_each = var.security_group_rules
    content {
      type        = ingress.value.type
      from_port   = ingress.value.from_port
      to_port     = ingress.value.to_port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
    }
  }
}


```

We define a list variable called security_group_rules, which contains a list of security group rules, each represented as an object with specific properties (e.g., type, from_port, to_port, protocol, cidr_blocks).

The aws_security_group resource is created with dynamic blocks for ingress rules. We use a dynamic block to iterate over each rule in the security_group_rules list and create corresponding ingress rules in the AWS security group.


## For-Each Loops

This looping construct allows you to create multiple instances of a resource based on a set of input values, such as a list or map. 

For-Each Loops Example:

In this example, we'll create AWS S3 buckets using a for-each loop based on a map of bucket names.

```
# Define a map of S3 bucket names
variable "s3_buckets" {
  description = "A map of S3 bucket names."
  type        = map(string)
  default = {
    "bucket-1" = "us-east-1"
    "bucket-2" = "us-west-2"
  }
}

# Create AWS S3 buckets using a for-each loop
resource "aws_s3_bucket" "example" {
  for_each = var.s3_buckets

  bucket = each.key
  acl    = "private"
  region = each.value
}
```

We define a map variable called s3_buckets, which contains a map of S3 bucket names, where the keys are bucket names, and the values are AWS regions.

The aws_s3_bucket resource is created using a for-each loop. We iterate over each key-value pair in the s3_buckets map and create an S3 bucket for each entry, setting the bucket name, ACL, and region based on the values in the map.




