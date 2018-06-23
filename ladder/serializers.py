from rest_framework import serializers
from .models import Tags,Ladder,Unit,User,Link,LearningStatus


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ('name',)

    def create(self,validated_data):
        return Tags(**validated_data)


class UserSerializer(serializers.ModelSerializer):

    my_link = serializers.SerializerMethodField()
    my_ladders = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('name','email','icon','profile','my_link','my_ladders')
        extra_kwargs = {'password':{'read_only':True}}


    def get_my_link(self,instance):
        serialize = {}
        list = []
        for ladder in instance.get_my_link():
            serialize = {'title':ladder.title,'tags':ladder.tags.name,'creater':ladder.creater.name,'created_at':ladder.created_at}
            list.append(serialize)
        return list

    def get_my_ladders(self,instance):
        serialize = {}
        list = []
        for ladder in instance.get_my_ladders():
            serialize = {'title':ladder.title,'tags':ladder.tags.name,'creater':ladder.creater.name,'created_at':ladder.created_at}
            list.append(serialize)
        return list


class LadderSerializer(serializers.ModelSerializer):

    unit = serializers.SerializerMethodField()
    recommended_prev_ladder = serializers.SerializerMethodField()
    recommended_next_ladder = serializers.SerializerMethodField()
    count_finish_number = serializers.SerializerMethodField()
    count_learning_number = serializers.SerializerMethodField()


    class Meta:
        model = Ladder
        fields = ('id','title','tags','is_public','creater','created_at','update_at','unit','recommended_prev_ladder','recommended_next_ladder','count_learning_number','count_finish_number')

    def get_unit(self,instance):
        serialize ={}
        list = []
        for unit in instance.get_unit():
            serialize = {'title':unit.title,'description':unit.description,'ladder':unit.ladder.title,'url':unit.url,'index':unit.index}
            list.append(serialize)
        return list

    def get_recommended_prev_ladder(self,instance):
        ladder = instance.get_recommended_prev_ladder()
        if ladder:
            return {'title':ladder.title,'tags':ladder.tags.name,'creater':ladder.creater.name,'created_at':ladder.created_at}
        else:
            return None

    def get_recommended_next_ladder(self,instance):
        ladder = instance.get_recommended_next_ladder()
        if ladder:
            return {'title':ladder.title,'tags':ladder.tags.name,'creater':ladder.creater.name,'created_at':ladder.created_at}
        else:
            return None

    def get_count_finish_number(self,instance):
        return instance.count_finish_number()

    def get_count_learning_number(self,instance):
        return instance.count_learning_number()




class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = ('title','description','ladder','url','index')


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = ('prior','latter','user')

    def validate(self,data):
        user = data['user']
        if data['latter'] in user.get_my_link().latter:
            raise serializers.ValidationError('登録済みです')
        return data



class LearningStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = LearningStatus
        fields = ('user','unit','status','created_at')
