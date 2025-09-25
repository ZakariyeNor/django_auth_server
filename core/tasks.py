import logging
from celery import shared_task
from oauth2_provider.models import AccessToken, RefreshToken
from django.utils import timezone

logger = logging.getLogger(__name__)

@shared_task
def cleanup_expired_tokens():
    now = timezone.now()

    # Delete expired access tokens
    expired_access = AccessToken.objects.filter(expires__lt=now)
    count_access = expired_access.count()
    expired_access.delete()

    # Delete orphaned refresh tokens
    expired_refresh = RefreshToken.objects.filter(access_token__isnull=True)
    count_refresh = expired_refresh.count()
    expired_refresh.delete()

    msg = f"[Celery] Cleaned {count_access} access tokens and {count_refresh} refresh tokens"
    logger.info(msg)

    return msg
