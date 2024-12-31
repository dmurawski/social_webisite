from django.contrib.contenttypes.models import ContentType
from .models import Action
import datetime
from django.utils import timezone


def create_action(user, verb, target=None):
    action = Action(user=user, verb=verb, target=target)
    action.save()
