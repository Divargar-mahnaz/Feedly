from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from core.pagination_handler import Pagination


class UserAPIView(APIView):
    """
    logged in user
    """
    permission_classes = [IsAuthenticated]


class NoAuthAPIView(APIView):
    """
    all users view
    """
    permission_classes = (BasePermission,)


class ListView(ListAPIView):
    pagination_class = Pagination

    def get_paginated_response(self, data):
        if not self.request.query_params.get('page'):
            return Response(data)
        return super().get_paginated_response(data)
