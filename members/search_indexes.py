from haystack import indexes
from members.models import Profile
from django.contrib.auth.models import User

class ProfileIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)
    user = indexes.CharField(model_attr='username')
    avatar = indexes.CharField(model_attr='avatar')
    city = indexes.CharField(model_attr='city')

    def get_model(self):
        return User
