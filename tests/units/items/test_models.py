from src.feedstocks.models import Item


class TestItem:
    def test_should_create_item_instance(self, item_model):
        assert isinstance(item_model, Item)
