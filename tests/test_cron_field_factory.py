import pytest

from cron_parser.cron_field_factory import CronFieldFactory
from cron_parser.cron_fields import CronFieldName, CronFieldAttribute, CronFieldType


@pytest.fixture(scope="class")
def cron_field_factory(valid_config_fixture):
    return CronFieldFactory(valid_config_fixture)


class TestCronFieldFactory:

    def test_get_cron_fields(self, cron_field_factory):
        cron_fields = cron_field_factory._get_cron_fields()

        assert len(cron_fields) == 5

    def test_get_cron_fields_empty_config(self, cron_field_factory, mocker):
        mock_config = mocker.patch("cron_parser.cron_field_factory.Config.get_var")
        mock_config.return_value = []

        cron_fields = cron_field_factory._get_cron_fields()

        assert len(cron_fields) == 0

    def test_group_by_field_name(self, cron_field_factory):
        res = cron_field_factory._group_by_field_name()
        for field_name in CronFieldName:
            assert field_name in res

    def test_get_field(self, cron_field_factory):
        field_name = CronFieldName.DAY_OF_MONTH
        field_value = "3"

        res = cron_field_factory.get_field(field_name, field_value)

        assert type(res) == CronFieldAttribute
        assert res.field_type == CronFieldType.NUMERIC
        assert res.min == 1
        assert res.max == 31

    def test_get_field_not_present(self, cron_field_factory):
        field_name = "1"
        field_value = "3"

        with pytest.raises(AssertionError) as exc:
            cron_field_factory.get_field(field_name, field_value)

        assert f"Invalid field name: {field_name} given" in str(exc.value)