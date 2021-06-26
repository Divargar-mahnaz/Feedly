from rest_framework import status
from rest_framework.exceptions import APIException

from common.common import ERROR_LIST
from common.messages import Account


class UserRegisterFailed(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = Account.REGISTER_USER_FAILED
    default_code = "{}{}-{}".format(ERROR_LIST['ACCOUNT'], status.HTTP_400_BAD_REQUEST, 1)


class UserNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = Account.INVALID_USERNAME_PASSWORD
    default_code = "{}{}-{}".format(ERROR_LIST['ACCOUNT'], status.HTTP_404_NOT_FOUND, 2)
