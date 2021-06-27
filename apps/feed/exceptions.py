from rest_framework import status
from rest_framework.exceptions import APIException

from common.common import ERROR_LIST
from common.messages import Feed


class FeedNotRegister(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = Feed.NOT_REGISTER
    default_code = "{}{}-{}".format(ERROR_LIST['Feed'], status.HTTP_400_BAD_REQUEST, 1)
