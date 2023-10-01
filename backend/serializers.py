from rest_framework import serializers
from .models import News, ImgFiles, GameDiscipline,User,Countries,Team

class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgFiles
        fields = ['file','name'] 

class ModelSerializerWithImg(serializers.ModelSerializer):
    img = ImgSerializer(read_only=True)

class NewsSerializers(ModelSerializerWithImg):
    class Meta:
        model = News
        fields = ['id','date','short_text','slug','img']

class CountriesSerializer(ModelSerializerWithImg):
    class Meta:
        model = Countries
        fields = ['img','name']

class GameDisciplineSerializer(ModelSerializerWithImg):
    class Meta:
        model = GameDiscipline
        fields = ["id","name","slug",'img']

class TeamSerializer(ModelSerializerWithImg):
    class Meta:
        model = Team
        fields = ["name","short_name",'img','tournaments','users']

class UserMaxInfoSerializer(ModelSerializerWithImg):
    team = TeamSerializer(read_only=True)
    main_game = GameDisciplineSerializer(read_only=True)
    country = CountriesSerializer(read_only=True)
    class Meta:
        model = User
        fields = '__all__'
class UserMinInfoSerializer(ModelSerializerWithImg):
    team = TeamSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id','name','img','team']