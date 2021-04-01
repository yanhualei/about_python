from rest_framework import serializers
from books.models import Author

class AuthorSerializer(serializers.Serializer):
    author_id = serializers.CharField(label='id')
    author_name = serializers.CharField(label="作者")
    phone = serializers.CharField(label="手机")
    created_time = serializers.DateTimeField(label="注册时间",read_only=True)


class AuthorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ["author_id","author_name","phone","created_time"]


class PrimaryKeySerializer(serializers.Serializer):
        authors = serializers.PrimaryKeyRelatedField(label="作者",queryset=Author.objects.all())

