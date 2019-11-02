from rest_framework import serializers

from ..models import Todo


class TodoListDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Todo
        fields = ('url', 'id', 'title', 'completed')


class TodoCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ('title', 'completed')
    
    def validate(self, data):
        return data
    
    def validate_title(self, value):
        data = self.get_initial()
        value = data.get('title')

        if not value:
            raise serializers.ValidationError("Title is required")

        return value
    
    def create(self, validated_data):
        Todo.objects.create(
            title=validated_data['title']
        )
        return validated_data
