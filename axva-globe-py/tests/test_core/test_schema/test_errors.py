import pytest

from core.schema.constants import Constants
from core.schema.errors import PartitionValueError


@pytest.mark.parametrize("partition",[-1, 0, 1])
def test_partition_value_error(partition):
    match_regex = f".*{partition}."
    with pytest.raises(PartitionValueError, match=match_regex):
        Constants(partition)
