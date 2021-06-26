from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class NoPagination(PageNumberPagination):

    def get_paginated_response(self, data):
        return Response(data)


class Pagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('all_page', self.page.paginator.num_pages),
            ('count', self.page.paginator.count),
            ('current', self.page.number),
            ('results', data)
        ]))
