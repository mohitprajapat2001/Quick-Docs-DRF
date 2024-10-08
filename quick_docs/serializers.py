from rest_framework import serializers
from quick_docs.models import Blog


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = self.context.get("request").query_params.get("fields")
        if fields is not None:
            fields = fields.split(",")
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class BlogSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
