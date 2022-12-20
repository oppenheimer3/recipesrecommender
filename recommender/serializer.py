from rest_framework.serializers import ModelSerializer
from .models import recipe

class recipeSerializer(ModelSerializer):
    class Meta:
        model=recipe
        fields='__all__'


