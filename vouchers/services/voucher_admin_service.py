# vouchers/services/voucher_admin_service.py
import logging

from botocore.exceptions import ClientError
from vouchers.model_voucher import Voucher

logger = logging.getLogger(__name__)

class VoucherAdminService:

    @staticmethod
    def register_new_vouchers(cleaned_data):
        try:
            voucher = Voucher(
                voucher_description=cleaned_data['voucher_description'],
                voucher_status=cleaned_data['voucher_status'],
                voucher_price=cleaned_data['voucher_price'],
                voucher_quantity=cleaned_data['voucher_quantity']
            )

            # invoke the method responsible to persist the data
            voucher.save_multiple_vouchers()

            return {'success': True,
                    'message': 'Vouchers created successfully.'}

        except ClientError as e:
            logger.error(f"AWS Error: {e}")
            return {'success': False,
                    'message': f"Cloud Provider Error: {str(e)}"}

        except Exception as e:
            logger.exception("Unexpected error during voucher creation")
            return {'success': False,
                    'message': 'An internal error occurred.'}
