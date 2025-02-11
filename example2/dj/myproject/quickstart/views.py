from rest_framework import permissions, viewsets
from myproject.quickstart.serializers import QuestionSerializer
from myproject.quickstart.models import Question

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
