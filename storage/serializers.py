from rest_framework import serializers
from .models import User, Task, SubTask


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'subtitle', 'subdone']


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(
        many=True, required=False)  # Subtasks verschachteln
    assigned = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned',
                  'due_date', 'priority', 'category', 'bucket', 'subtasks']

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        task = Task.objects.create(**validated_data)

        for subtask_data in subtasks_data:
            SubTask.objects.create(task=task, **subtask_data)

        return task

    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if subtasks_data:
            instance.subtasks.all().delete()  # Alte Subtasks löschen
            for subtask_data in subtasks_data:
                SubTask.objects.create(task=instance, **subtask_data)

        return instance
