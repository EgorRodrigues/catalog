from typing import List

from src.compositions.models import Composition, Feedstock, Service


class TestService:
    def test_should_create_service_instance(self, composition_model):
        assert isinstance(composition_model, Composition)

    def test_if_the_feedstock_items_are_of_the_feedstock_type(self, composition_model):
        assert isinstance(composition_model.feedstock[0], Feedstock)

    def test_if_the_service_items_are_of_the_service_type(self, composition_model):
        assert isinstance(composition_model.services[0], Service)
