from rest_framework import status,viewsets,filters,permissions
from .models import Tags,User,Ladder,Unit,Link,LearningStatus
from .serializers import TagsSerializer,LadderSerializer,UserSerializer,UnitSerializer,LinkSerializer,LearningStatusSerializer
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class LadderFilter(filters.FilterSet):
    creater = filters.CharFilter(name='creater',lookup_expr='exact')

    class Meta:
        model = Ladder
        fields = ['creater']


class LadderViewSet(viewsets.ModelViewSet,permissions.BasePermission):
    queryset = Ladder.objects.all().filter(is_public=True)
    serializer_class = LadderSerializer
    filter_class = LadderFilter
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class LearningStatusViewSet(viewsets.ModelViewSet):
    queryset = LearningStatus.objects.all()
    serializer_class = LearningStatusSerializer
