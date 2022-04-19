from django.urls import path
from . import views


urlpatterns = [
    path(
        "dataform/<int:pk>/detail/item/create",
        views.ItemCreateView.as_view(),
        name="item-create",
    )
]
