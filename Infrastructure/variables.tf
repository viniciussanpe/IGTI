variable "aws_region" {
  default = "us-east-2"
}

variable "lambda_function_name" {
  default = "IGTIexecutaEMRaovivo"
}

variable "key_pair_name" {
  default = "my-vpc-igti-mod1"
}

variable "airflow_subnet_id" {
  default = "subnet-2e4f9145"
}

variable "vpc_id" {
  default = "vpc-5d71c736"
}
