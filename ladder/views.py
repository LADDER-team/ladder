from rest_framework import status,viewsets,filters,permissions,authentication
from .models import Tags,User,Ladder,Unit,Link,LearningStatus
from .serializers import TagsSerializer,LadderSerializer,UserSerializer,UnitSerializer,LinkSerializer,LearningStatusSerializer
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
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
    permission_classes = (IsOwnerOrReadOnly,)

    def create(self, request, *args, **kwargs):
        if {'title':request.data['title']} in Ladder.objects.filter(creater=request.user.pk).values('title'):
            raise ValidationError('同じタイトルのLADDERが投稿されています')
        add_data = request.data.copy()
        add_data['creater'] = request.user.pk
        serializer = self.get_serializer(data=add_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        add_data = request.data.copy()
        add_data['creater'] = request.user.pk
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=add_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)



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
    permission_classes = (IsOwnerOrReadOnly,)

    def create(self, request, *args, **kwargs):
        if {'latter':int(request.data['latter'])} in Link.objects.filter(user=request.user.pk).values('latter'):
            raise ValidationError('既にこのLADDERはペグされています')
        add_data = request.data.copy()
        add_data['user'] = request.user.pk
        serializer = self.get_serializer(data=add_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        add_data = request.data.copy()
        add_data['user'] = request.user.pk
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=add_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class LearningStatusViewSet(viewsets.ModelViewSet):
    queryset = LearningStatus.objects.all()
    serializer_class = LearningStatusSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

    def create(self, request, *args, **kwargs):
        if {'unit':int(request.data['unit'])} in LearningStatus.objects.filter(user=request.user.pk).values('unit'):
            raise ValidationError('同じタイトルのLADDERが投稿されています')
        add_data = request.data.copy()
        add_data['user'] = request.user.pk
        serializer = self.get_serializer(data=add_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        add_data = request.data.copy()
        add_data['user'] = request.user.pk
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=add_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

def index(request):
    return render(request, 'index.html', {})
