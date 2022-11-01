from rest_framework import mixins, viewsets


class CreateListGenericRetrieveViewSet(mixins.CreateModelMixin,
                                       mixins.ListModelMixin,
                                       viewsets.GenericViewSet):
    pass
