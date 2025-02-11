from rest_framework import serializers
from myproject.quickstart.models import Question

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
