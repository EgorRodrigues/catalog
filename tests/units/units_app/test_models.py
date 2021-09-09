from src.units.models import Unit


class TestUnit:
    def test_should_create_unit_instance(self, unit_model):
        assert isinstance(unit_model, Unit)
