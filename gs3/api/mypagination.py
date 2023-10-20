from rest_framework.pagination import LimitOffsetPagination



class MyLimitOffsetPagination(LimitOffsetPagination):
   default_limit = 3
   limit_query_param = 'limit'
   offset_query_param = 'myoffset'
   max_limit = 10
