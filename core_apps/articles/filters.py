import django_filters as filters
from core_apps.articles.models import Article
from taggit.managers import TaggableManager

class ArticleFilter(filters.FilterSet):
    author = filters.CharFilter(
        field_name="author__first_name",lookup_expr="icontains"
    )
    title = filters.CharFilter(field_name="title",lookup_expr="icontains")
    tag = filters.CharFilter(field_name="tags__name",lookup_expr="iexact")
    created_at=filters.DateFromToRangeFilter(field_name="created_at")
    updated_at=filters.DateFromToRangeFilter(field_name="updated_at")

    class Meta:
        model=Article
        fields=["author","title","tags","created_at","updated_at"]

        filter_overrides = {
            TaggableManager: {
                "filter_class": filters.CharFilter,
                "extra": lambda f: {
                    "lookup_expr": "icontains",
                },
            },
        }

