from haystack import indexes
from tutorials.models import Question


class QuestionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    message = indexes.CharField(model_attr='message')
    slug = indexes.CharField(model_attr='slug')
    validate = indexes.CharField(model_attr='validate')
    picture = indexes.CharField(model_attr='picture')
    user = indexes.CharField(model_attr='user_id')
    date = indexes.CharField(model_attr='date')

    def get_model(self):
        return Question

    #def index_queryset(self, using=None):
    #    """Used when the entire index for model is updated."""
    #    return self.get_model().objects