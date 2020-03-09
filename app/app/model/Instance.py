class instance():
    def __init__(self,image,platform,ec2_type,public_dns_name,status,private_ip_address,name,id,key):
        self.id = id
        self.key = key
        self.name = name
        self.image = image
        self.status = status
        self.type = ec2_type
        self.platform = platform
        self.public_dns_name = public_dns_name
        self.private_ip_address = private_ip_address