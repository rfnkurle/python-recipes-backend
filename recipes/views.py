from django.shortcuts import render
from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeView(APIView):
    #target single recipe
    def get_recipe(self, pk):
       try:
        recipe = Recipe.objects.get(recipeId=pk)
        return recipe
       except Recipe.DoesNotExist:
        raise Http404
    # get all reipes
    def get(self, request, pk=None):
       if pk:
        data = self.get_recipe(pk)
        serializer = RecipeSerializer(data)
       else:
        data = Recipe.objects.all()
        serializer = RecipeSerializer(data, many=True)
       return Response(serializer.data)
   
    def post(self, request):
        data = request.data
        serializer = RecipeSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Recipe Added Successfully", safe=False)
        return JsonResponse("Failed to Add Recipe", safe=False)
    
    def delete(self, request, pk):
      recipe_to_delete = Recipe.objects.get(recipeId=pk)
      recipe_to_delete.delete()
      return JsonResponse("Recipe Deleted Successfully", safe=False)
    
  
