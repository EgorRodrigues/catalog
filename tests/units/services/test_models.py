from src.services.models import Service


class TestService:
    def test_should_create_service_instance(self, service_model):
        assert isinstance(service_model, Service)
