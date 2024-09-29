from rest_framework.response import Response


class ListReportModelMixin:
    def list(self, request, *args, **kwargs):
        
        queryset = self.filter_queryset(self.get_queryset())
        accept = queryset.filter(is_accept=True)
        not_accept = queryset.filter(is_accept=False)
        accept_serializer = self.get_serializer(accept, many=True)
        not_accept_serializer = self.get_serializer(not_accept, many=True)
        
        return Response({
            "accept": accept_serializer.data,
            "not_accepted": not_accept_serializer.data,
        })
