'''
This class defines methods to handle AWS
CFN stack creation
@since 28-11-2018
@author amit.dali@gmail.com
'''
import boto3
import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class DeployTemplate:
	
	def __init__(self):
		pass
	
	def generateStackName(self):
		timestamp =  str(int(time.time()))
		stackName = 'blueprint-buddy-' + timestamp
		logger.info('StackName:%s',stackName)
		return stackName
		
	def createStack(self):
		logger.info('createStack')
		client = boto3.client('cloudformation')
		ec2Template = open('../templates/aws/ec2.yml',mode='r')
		ec2CreateTemplate = ec2Template.read()
		ec2Template.close()
		stackName = self.generateStackName()
		response = client.create_stack(
					StackName = stackName,
					TemplateBody = ec2CreateTemplate
					)
		