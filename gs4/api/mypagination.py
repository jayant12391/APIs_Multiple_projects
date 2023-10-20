from rest_framework.pagination import CursorPagination



class MyCursorPagination(CursorPagination):
   page_size = 3
   ordering = 'name'  # eg. 'name' & 'id'
   cursor_query_param = 'c'
