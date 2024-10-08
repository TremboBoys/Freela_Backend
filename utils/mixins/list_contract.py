from rest_framework.response import Response

class ListContractModelMixin:
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        free = queryset.filter(type_of_service=1)
        month_group = queryset.filter(type_of_service = 2)
        year_group = queryset.filter(type_of_service= 3)
        free_serializer = self.get_serializer(free, many=True)
        month_serializer = self.get_serializer(month_group, many=True)
        year_serializer = self.get_serializer(year_group, many=True)

        return Response({
            "free": free_serializer.data,
            "month": month_serializer.data, 
            "year": year_serializer.data 
        })
