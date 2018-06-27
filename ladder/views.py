from rest_framework import status,viewsets,filters,permissions,authentication
from .models import Tags,User,Ladder,Unit,Link,LearningStatus
from .serializers import TagsSerializer,LadderSerializer,UserSerializer,UnitSerializer,LinkSerializer,LearningStatusSerializer
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from django.shortcuts import render


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.creater == request.user


class LadderFilter(filters.FilterSet):
    creater = filters.CharFilter(name='creater',lookup_expr='exact')

    class Meta:
        model = Ladder
        fields = ['creater']


class LadderViewSet(viewsets.ModelViewSet,permissions.BasePermission):
    queryset = Ladder.objects.all().filter(is_public=True)
    serializer_class = LadderSerializer
    filter_class = LadderFilter
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)


class LearningStatusViewSet(viewsets.ModelViewSet):
    queryset = LearningStatus.objects.all()
    serializer_class = LearningStatusSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)


def index(request):
    return render(request, 'index.html', {})
