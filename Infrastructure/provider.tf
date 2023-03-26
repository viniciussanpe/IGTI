provider "aws" {
    region = "us-east-2"
}

terraform {
    backend "s3" {
        bucket = "terraforma-state-igti-vini"
        key = "state/igti/edc/mod1/terraform.tfstate"
        region = "us-east-2"
    }
}