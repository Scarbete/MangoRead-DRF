from rest_framework.pagination import LimitOffsetPagination


class MangaPagination(LimitOffsetPagination):
    default_limit = 2400
    max_limit = 2400
