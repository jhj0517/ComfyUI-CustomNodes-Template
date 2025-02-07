import pytest


@pytest.mark.parametrize(
    "var_a,var_b",
    [
        (1, 2),
    ]
)
def test_basic(
    var_a: int,
    var_b: int,
):
    assert var_a + var_b == 3,  f"Test failed, var_a + var_b = {var_a + var_b}"
    assert var_a - var_b == -1,  f"Test failed, var_a - var_b = {var_a - var_b}"