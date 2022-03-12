from typing import Union, Dict, List

from cron_parser.config import Config
from cron_parser.cron_fields import CronFieldAttribute, CronFieldName, CronFieldType
from cron_parser.exceptions import InvalidFieldValue


class CronFieldFactory:

    def __init__(self, config: Config):
        self._config = config
        self._cron_field_map_by_name = self._group_by_field_name()

    @staticmethod
    def get_cron_field_type(field_val: str) -> CronFieldType:
        for elem in CronFieldType:
            if elem.value.match(field_val):
                return elem

        raise InvalidFieldValue(f"Invalid field value for field with value: {field_val}")

    def get_field(self, field_name: CronFieldName, field_val: str) -> CronFieldAttribute:
        field_type = CronFieldFactory.get_cron_field_type(field_val)

        assert field_name in self._cron_field_map_by_name, f"Invalid field name: {field_name} given"

        field_config = self._cron_field_map_by_name[field_name]

        range_min: int = field_config.get('min')
        range_max: int = field_config.get('max')

        if not field_type:
            raise InvalidFieldValue(f"Invalid field value for field: {field_name.name} given")

        return CronFieldAttribute(
            field_name,
            field_type,
            field_val,
            range_min,
            range_max
        )

    def _get_cron_fields(self) -> List[Dict[str, Union[str, int]]]:
        return self._config.get_var('fields')

    def _group_by_field_name(self):
        cron_fields = self._get_cron_fields()
        if not cron_fields:
            raise ValueError("Unable to fetch config fror cron_fields")
        return {CronFieldName[field.get("field_name")]: field for field in cron_fields}
