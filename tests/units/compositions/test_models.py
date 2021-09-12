from src.compositions.models import Composition


class TestService:
    def test_should_create_service_instance(self, composition_model):
        assert isinstance(composition_model, Composition)
