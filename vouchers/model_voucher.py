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


    def _generate_item_dict(self):
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
                    batch.put_item(Item=self._generate_item_dict())
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

    @staticmethod
    def find_voucher_by_id(voucher_id):
        try:
            table = Voucher._get_table().get_item(Key={'voucher_id': voucher_id})
            response = table.get('Item', {})
            return response

        except ClientError as e:
            error_code = e.response['Error']['Code']
            logger.error(f"Error on DynamoDB [{error_code}]: {e}")
            return []


    @staticmethod
    def edit_voucher(cleaned_data, voucher_id):

        print(cleaned_data)
        if not voucher_id:
            return {"success": False, "error": "Voucher_id not found"}

        try:
            table = Voucher._get_table().update_item(
                Key={'voucher_id': voucher_id},
                UpdateExpression="SET "
                                 "voucher_status = :val_status,"
                                 "voucher_price = :val_price,"
                                 "voucher_description = :val_description,"
                                 "voucher_tx_hash = :val_tx_hash",
                ExpressionAttributeValues={
                    ':val_status': cleaned_data.get('voucher_status'),
                    ':val_price': cleaned_data.get('voucher_price'),
                    ':val_description': cleaned_data.get('voucher_description'),
                    ':val_tx_hash': '',
                },
                ReturnValues='UPDATED_NEW'
            )
            return {"success": True, "voucher_id": voucher_id,
                    "table" : table,
                    "message": "Voucher_id updated successfully"}

        except ClientError as e:
            error_code = e.response['Error']['Code']
            logger.error(f"Error on DynamoDB [{error_code}]: {e}")
            return {"success": False, "error": "voucher_id not found"}

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return {"success": False, "error": f"Unexpected error: {e}"}