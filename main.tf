provider "aws" {
  region = "us-east-1"
}

variable "BUCKET_NAME" {}

resource "aws_s3_bucket" "example" {
  bucket = "12yefgg124rnb2q4"
}
