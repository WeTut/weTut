from haystack import indexes
from members.models import Profile
from django.contrib.auth.models import User

class UserIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True)
	username = indexes.CharField(model_attr='username')

	def get_model(self):
		return User

