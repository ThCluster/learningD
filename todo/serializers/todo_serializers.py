from rest_framework import serializers
from todo.models.todo import Todo

class TodoSerializer(serializers.ModelSerializer):
    
    # due_date = serializers.DateField(source='due_date', format='%Y-%m-%d', input_formats=['%Y-%m-%d'], required=False, allow_null=True)
    class Meta:
        model = Todo
        fields = '__all__'
        # exclude = ['due_date'] suppression d'un champ qu'on ne veut pas afficher dans le serializer, mais on peut le laisser dans le model pour la base de données