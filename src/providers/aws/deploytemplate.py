'''
This class defines methods to handle AWS
CFN stack creation
@since 28-11-2018
@author amit.dali@gmail.com
'''
import boto3
import logging

class DeployTemplate:
	logger = logging.getLogger()
	logger.setLevel(logging.INFO)
	
	def __init__(self):
		pass
	
	def generateStackName():
		timestamp = int(time.time())
		stackName = 'blueprint-buddy-' + timestamp
		logger.info('StackName:%s',stackName)
		return stackName
		
	def createStack():
		ec2Template = file.open('../../templates/aws/ec2.yml',mode='r')
		ec2CreateTemplate = ec2Template.read()
		file.close()
		response = client.create_stack(
					StackName = generateStackName(),
					TemplateBody = ec2CreateTemplate
					)
		