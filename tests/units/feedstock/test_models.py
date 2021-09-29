from src.feedstock.models import Feedstock


class TestFeedstock:
    def test_should_create_feedstock_instance(self, feedstock_model):
        assert isinstance(feedstock_model, Feedstock)
