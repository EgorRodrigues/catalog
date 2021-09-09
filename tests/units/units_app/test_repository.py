from src.units.repository import Repository


class TestRepository:
    def test_should_be_a_repository(self, fake_repository):
        assert isinstance(fake_repository, Repository)
