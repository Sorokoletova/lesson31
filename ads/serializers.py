from rest_framework import serializers
from ads.models import Categorie, Ads, Selection


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class AdsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        many=False,
        slug_field="username"
    )
    category = serializers.SlugRelatedField(
        read_only=True,
        many=False,
        slug_field="name"
    )

    class Meta:
        model = Ads
        fields = '__all__'


class AdsCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Ads
        exclude = ["image"]


class AdsUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ads
        exclude = ["image"]


class AdsDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ["id"]

class AdsUploadeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ["id"]


class SelectionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Ads
        fields = ['id','name']


class SelectionDetailSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=True,
        many=False,
        slug_field="username"
    )
    items = AdsSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = Selection
        fields = '__all__'

class SelectionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id"]

