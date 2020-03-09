from flask_jwt import JWT, jwt_required, current_identity
from flask import Flask,request, jsonify, render_template
from botocore.exceptions import ClientError
from flask_cors import CORS, cross_origin
from controller import auth
from model import Instance
from model import Buckets
import datetime,json
import boto3

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['SECRET_KEY'] = 'c55e0ede04a5b61b4b8e14224621fa07'
jwt = JWT(app, auth.authenticate, auth.identity)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/status',methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def status():
    data={"status":"success"}
    response = app.response_class(
        status=200,
        response=json.dumps(data),
        mimetype='application/json'
    )
    return response

@app.route('/profile')
@cross_origin(supports_credentials=True)
@jwt_required()
def profile():
    data = {'name':'%s' %current_identity} 
    response = app.response_class(
        status=200,
        response=json.dumps(data),
        mimetype='application/json'
    )
    return response

@app.route('/s3/buckets',methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def getBucket():
  s3 = getResourceS3()
  list = []
  try:
    for bucket in s3.buckets.all():
      list.append(Buckets.buckets(bucket.name,bucket.creation_date))
    return jsonify([ob.__dict__ for ob in list])
  except ClientError as e:
    data = {"status":"fail","message":"region not available"}
    response = app.response_class(
        status=404,
        response=json.dumps(data),
        mimetype='application/json'
    )
    return response
       
@app.route('/region',methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def getRegion():
  ec2 = getRegion()
  enabled_regions = ec2.get_available_regions('ec2')
  response = app.response_class(
        status=200,
        response=json.dumps(enabled_regions),
        mimetype='application/json'
  )
  return response
    
@app.route('/ec2/instance/<region>',methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def getInstance(region):
  ec2 = getResourceEc2(region)
  list = []
  try:
    for instances in ec2.instances.all():
      Instances= Instance.instance(
                 instances.image.name,
                 instances.platform,
                 instances.instance_type,
                 instances.public_dns_name,
                 instances.state.get("Name"),
                 instances.private_ip_address,
                 instances.tags[0].get("Value"),
                 instances.id,instances.key_name)
      list.append(Instances)
    return jsonify([ob.__dict__ for ob in list])
  except ClientError as e:
    data = {"status":"fail","message":"region not available"}
    response = app.response_class(
        status=404,
        response=json.dumps(data),
        mimetype='application/json'
    )
    return response
       
    
def getResourceEc2(region):
  ec2 = boto3.resource(
    'ec2',
     region_name=region,
     aws_access_key_id='AKIA3HJRQHXKTUF7Z3U6' ,
     aws_secret_access_key='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'
  )
  return ec2 

def getResourceS3():
  s3 = boto3.resource(
     's3',
     aws_access_key_id='AKIA3HJRQHXKTUF7Z3U6' ,
     aws_secret_access_key='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'
  )
  return s3 

def getRegion():
  Region = boto3.Session(
     aws_access_key_id='AKIA3HJRQHXKTUF7Z3U6' ,
     aws_secret_access_key='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'
  )
  return Region 

def default(o):
    if type(o) is datetime.date or type(o) is datetime.datetime:
        return o.isoformat()


if __name__ == "__main__":
   app.run()
