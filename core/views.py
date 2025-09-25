from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from oauth2_provider.models import AccessToken


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    return Response({
        'username': user.username,
        'email': user.email,
        "id": user.id,
    })

@api_view(['POST'])
def logout(request):
    token = request.auth
    if token:
        token.delete()
    return Response({"detail": "Successfully user logged out."})