from .recommender import recipes_recommender
from .models import recipe
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import recipeSerializer

@api_view(['POST'])
def recommend(request):
    data=request.data
    liked=list(map(int, data))
    recommended_ids=recipes_recommender(liked)
    recipes=recipe.objects.filter(id__in=recommended_ids)
    serialized=recipeSerializer(recipes,many=True)
    return Response(serialized.data)

@api_view(['POST'])
def getliked(request):
    data=request.data
    liked=list(map(int, data))
    recipes=recipe.objects.filter(id__in=liked)
    serialized=recipeSerializer(recipes,many=True)
    return Response(serialized.data)

@api_view(['GET'])
def allrecipes(request):
    recipes=recipe.objects.all()[0:50]
    serialized=recipeSerializer(recipes,many=True)
    return Response(serialized.data)
@api_view(['GET'])
def recipespage(request,p):
    x=p*50+50
    recipes=recipe.objects.all()[x-50:x]
    serialized=recipeSerializer(recipes,many=True)
    return Response(serialized.data)

@api_view(['GET'])
def getrecipe(request,id):
    recipes=recipe.objects.get(id=id)
    serialized=recipeSerializer(recipes,many=False)
    return Response(serialized.data)

@api_view(['GET'])
def recipes(request,title):
    title=title.replace('+',' ')
    recipes=recipe.objects.filter(title__icontains=title)
    serialized=recipeSerializer(recipes,many=True)
    return Response(serialized.data)
