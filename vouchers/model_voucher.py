# vouchers/model_voucher.py

import uuid
import logging
import boto3
from botocore.exceptions import ClientError, BotoCoreError

logger = logging.getLogger(__name__)

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
            'voucher_status': str(self.voucher_status),
            'voucher_tx_hash': '',
        }


    def save_multiple_vouchers(self):
        try:
            table = self._get_table()
            with table.batch_writer() as batch:
                for _ in range(int(self.voucher_quantity)):
                    batch.put_item(Item=self.to_dict())
            return True

        except ClientError as e:
            error_code = e.response['Error']['Code']
            logger.error(f"Error on DynamoDB [{error_code}]: {e}")
            raise

        except BotoCoreError as e:
            logger.error(f"Error on SDK Boto3: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise


    @staticmethod
    def list_vouchers_by_status():
        try:
            table = Voucher._get_table()
            response = table.scan()
            return response.get('Items', [])

        except ClientError as e:
            error_code = e.response['Error']['Code']
            logger.error(f"Error on DynamoDB [{error_code}]: {e}")
            return []