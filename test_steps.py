

# you can use pytest_steps.test_steps to give you flow control of tests: carrying out one in one condition, and another in another condition

# requires pip3 install pytest-steps

from pytest_steps import test_steps


def sum(n1, n2):
    return n1 + n2


def average_2_nums(sum):
    return sum / 2


def sum_test(steps_data):
    res = sum(1, 3)
    assert res == 4
    steps_data.res = res


def perc_difference_test(steps_data):
    avg = average_2_nums(steps_data.res)
    assert avg == 2


# this test will call the functions sum_test and perc_difference_test as tests
@test_steps(sum_test, perc_difference_test)
def test_calc_suite(test_step, steps_data):
    if test_step == 'sum_test':
        sum_test(steps_data)
    elif test_step == 'perc_difference_test':
        perc_difference_test(steps_data)


