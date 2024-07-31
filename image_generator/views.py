from rest_framework import generics
from rest_framework.response import Response
from .models import TestUser
from .serializers import TestUserSerializer, GenerateImageSerializer
from rest_framework import status
from .tasks import generate_image

class TestUserAdd(generics.ListCreateAPIView):
    queryset = TestUser.objects.all()
    serializer_class = TestUserSerializer

class TestUserList(generics.ListAPIView):
    queryset = TestUser.objects.all()
    serializer_class = TestUserSerializer

class GenerateImageView(generics.CreateAPIView):
    serializer_class = GenerateImageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        prompts = serializer.validated_data['prompts']

        # Trigger Celery tasks for each prompt
        task_ids = []
        for prompt in prompts:
            task = generate_image.delay(prompt)
            task_ids.append(task.id)

        return Response({'task_ids': task_ids}, status=status.HTTP_202_ACCEPTED)