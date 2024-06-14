variable "os" {
  type = string
  default = "ami-08a0d1e16fc3f61ea"
  description = "This is my ami ID"
}

variable "size" {
  default = "t2.micro"
}

variable "instance_name" {
    default = "TerraformEC2"
}

# variable "bucket_name" {
  
# }

variable "username" {
  
}