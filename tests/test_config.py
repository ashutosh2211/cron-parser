import os

import pytest

from cron_parser.config import Config

FIXTURES_PATH = "tests/fixtures"
DIRECTORY = os.getcwd()


class TestConfig:

    def test_config_with_path(self, valid_config_fixture):
        assert len(valid_config_fixture.get_var("fields")) == 5

    def test_config_with_invalid_path(self):
        path = "test"

        with pytest.raises(AssertionError) as exc:
            config = Config(path)

    def test_config_with_missing_var(self, valid_config_fixture):
        with pytest.raises(ValueError) as exc:
            val = valid_config_fixture.get_var("a")
