import boto3
from botocore.exceptions import ClientError

class DynamoDBManager:
    def __init__(self, region_name='us-east-1'):
        self.dynamodb = boto3.resource('dynamodb', region_name=region_name)
        self.events_table = self.dynamodb.Table('events')
        self.registrations_table = self.dynamodb.Table('registrations')

    def get_all_events(self):
        try:
            response = self.events_table.scan()
            return response.get('Items', [])
        except ClientError as e:
            print(f"Unable to fetch events: {e}")
            return None

    def get_all_registrations(self):
        try:
            response = self.registrations_table.scan()
            return response.get('Items', [])
        except ClientError as e:
            print(f"Unable to fetch registrations: {e}")
            return None

    def get_event_by_id(self, event_id):
        try:
            response = self.events_table.get_item(Key={'id': event_id})
            return response.get('Item', None)
        except ClientError as e:
            print(f"Unable to fetch event with ID {event_id}: {e}")
            return None

    def get_registration_by_id(self, registration_id):
        try:
            response = self.registrations_table.get_item(Key={'id': registration_id})
            return response.get('Item', None)
        except ClientError as e:
            print(f"Unable to fetch registration with ID {registration_id}: {e}")
            return None

    def post_event(self, event_data):
        try:
            self.events_table.put_item(Item=event_data)
            return f"Event {event_data['id']} added successfully."
        except ClientError as e:
            print(f"Unable to add event: {e}")
            return None

    def post_registration(self, registration_data):
        try:
            self.registrations_table.put_item(Item=registration_data)
            return f"Registration {registration_data['id']} added successfully."
        except ClientError as e:
            print(f"Unable to add registration: {e}")
            return None
