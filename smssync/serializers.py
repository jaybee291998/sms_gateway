from rest_framework import serializers

from .models import Gateway, Task

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class TaskSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskPostSerializer(serializers.Serializer):
	api_key 		= serializers.CharField(max_length=13)
	to 				= serializers.CharField(max_length=32)
	message			= serializers.CharField(max_length=2048)