import boto3
import os
import json


class Queue():
	def __init__(self) -> None:
		self.sqs = boto3.client('sqs')


	def send(self, url: str, message: dict, group_id: int) -> dict:

		response = self.sqs.send_message(
				QueueUrl = url,
				MessageBody = json.dumps(message),
				MessageGroupId = str(group_id)
			)

		return response


	def delete(self, queue_url: str, receipt_handle: str):
		
		response = self.sqs.delete_message(
				QueueUrl = queue_url,
				ReceiptHandle = receipt_handle
			)

		return response
