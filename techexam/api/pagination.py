from rest_framework import pagination

class CustomPageNumberPagination(pagination.PageNumberPagination):

    page_query_param = 'page'
    page_size_query_param = 'per_page'

