resource "aws_instance" "web" {
    ami = var.os #linux
    instance_type = var.size #t2.micro
 
tags = {
    Name = var.instance_name
}
}

# resource "aws_s3_bucket" "bucket" {
#    bucket = var.bucket_name
#  }

# to pass parameters while executing the plan
# terraform plan -var="bucket_name=mysecondbucket" 

resource "aws_iam_user" "myuser" {
    name = "${var.username}-user"
}


output "IPaddress" {
  value = aws_instance.web.public_ip
}

output "DNS" {
  value = aws_instance.web.public_dns
}