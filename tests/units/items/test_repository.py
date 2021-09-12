from src.feedstocks.repository import Repository


class TestItem:
    def test_should_be_a_repository(self, fake_repository):
        assert isinstance(fake_repository, Repository)
