
# //model serializers

from rest_framework import serializers
from FirstApp.models import userContact


class userContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = userContact
        fields = ["id", 'name', 'email', 'phone']

# //views
