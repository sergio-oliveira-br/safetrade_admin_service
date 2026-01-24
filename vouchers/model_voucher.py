import uuid
import boto3
from boto3.dynamodb.conditions import Key

from vouchers.choices import VoucherStatus, CountryCode

# Create your models here.

class Voucher:

    def __init__(self, voucher_description, voucher_price, voucher_quantity, voucher_status, voucher_location):
        # self.voucher_id = str(uuid.uuid4())[:8].upper()
        self.voucher_description = voucher_description
        self.voucher_price = str(voucher_price)
        self.voucher_quantity = voucher_quantity
        self.voucher_status = voucher_status
        self.voucher_location = voucher_location


    def to_dict(self):
        """Converts the object to the format that DynamoDB supports"""
        return {
            'voucher_id': str(uuid.uuid4())[:8].upper(),
            'voucher_description': self.voucher_description,
            'voucher_price': self.voucher_price,
            'voucher_quantity': self.voucher_quantity,
            'voucher_status': str(self.voucher_status),
            'voucher_location': str(self.voucher_location)
        }


    def save(self):
        dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
        table = dynamodb.Table('vouchers_db')
        return table.put_item(Item=self.to_dict())

    def save_multiple_vouchers(self):
        dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
        table = dynamodb.Table('vouchers_db')

        with table.batch_writer() as batch:
            for _ in range(int(self.voucher_quantity)):
                batch.put_item(Item=self.to_dict())

    @staticmethod
    def list_vouchers_by_location(location_code):
        # table = boto3.resource('dynamodb', region_name='eu-west-1').Table('vouchers_db')
        dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
        table = dynamodb.Table('vouchers_db')

        response = table.query(
            KeyConditionExpression=Key('voucher_location').eq(location_code))

        return response.get('Items', [])

