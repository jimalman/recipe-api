"""
Views for the Recipe APIs
"""
from rest_framework import (
    viewsets,
    mixins,
)

from rest_framework.permissions import IsAuthenticated

from core.models import (
    Recipe,
    Tag,
    Ingredient,
)

from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """ View for manage recipe APIs."""
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ Retrieve recipes for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request"""
        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save(user=self.request.user)


class TagViewSet(mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    """ View for managing Tag APIs """
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ Retrieve Tags for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')


class IngredientViewSet(mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    """ View for manage ingredients """
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ Retrieve Tags for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
