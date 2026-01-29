import uuid
import boto3
from boto3.dynamodb.conditions import Key

# Create your models here.
class Voucher:

    # AWS Details
    _TABLE_NAME = 'vouchers_db'
    _REGION = 'eu-west-1'

    @classmethod
    def _get_table(cls):
        dynamodb = boto3.resource('dynamodb', region_name=cls._REGION)
        return dynamodb.Table(cls._TABLE_NAME)

    def __init__(self, voucher_description, voucher_price, voucher_quantity, voucher_status):
        # self.voucher_id = str(uuid.uuid4())[:8].upper()
        self.voucher_description = voucher_description
        self.voucher_price = str(voucher_price)
        self.voucher_quantity = voucher_quantity
        self.voucher_status = voucher_status


    def to_dict(self):
        """Converts the object to the format that DynamoDB supports"""
        return {
            'voucher_id': str(uuid.uuid4())[:8].upper(),
            'voucher_description': self.voucher_description,
            'voucher_price': self.voucher_price,
            'voucher_quantity': self.voucher_quantity,
            'voucher_status': str(self.voucher_status),
        }


    def save(self):
        table = self._get_table()

        return table.put_item(Item=self.to_dict())


    def save_multiple_vouchers(self):
        table = self._get_table()
        with table.batch_writer() as batch:
            for _ in range(int(self.voucher_quantity)):
                batch.put_item(Item=self.to_dict())


    @staticmethod
    def list_vouchers_by_status(status_code):
        table = Voucher._get_table()
        response = table.query(KeyConditionExpression=Key('voucher_status').eq(status_code))

        return response.get('Items', [])

