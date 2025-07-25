import unittest
from test import compute_average

class TestComputeAverage(unittest.TestCase):
    """compute_average 함수에 대한 단위 테스트 클래스."""

    def test_positive_integers(self):
        """양의 정수 리스트로 평균을 올바르게 계산하는지 테스트합니다."""
        self.assertEqual(compute_average([1, 2, 3, 4, 5]), 3.0)

    def test_mixed_numbers(self):
        """양수와 음수가 섞인 리스트의 평균을 테스트합니다."""
        self.assertEqual(compute_average([-1, 1, -2, 2, 5]), 1.0)

    def test_floating_point_numbers(self):
        """부동소수점 숫자를 포함한 리스트의 평균을 테스트합니다."""
        # 부동소수점 비교 시 발생할 수 있는 미세한 오차를 처리하기 위해 assertAlmostEqual 사용
        self.assertAlmostEqual(compute_average([0.5, 1.5, 2.5]), 1.5)

    def test_list_of_zeros(self):
        """모든 요소가 0인 리스트의 평균을 테스트합니다."""
        self.assertEqual(compute_average([0, 0, 0, 0]), 0.0)

    def test_single_element_list(self):
        """요소가 하나인 리스트의 평균을 테스트합니다."""
        self.assertEqual(compute_average([100]), 100.0)

    def test_empty_list_raises_error(self):
        """빈 리스트가 주어졌을 때 ZeroDivisionError가 발생하는지 테스트합니다."""
        # with self.assertRaises(...) 컨텍스트 매니저를 사용하여
        # 특정 예외가 발생하는지 확인할 수 있습니다.
        with self.assertRaises(ZeroDivisionError):
            compute_average([])


# 이 파일을 직접 실행할 때 테스트를 실행하기 위한 구문
if __name__ == '__main__':
    unittest.main()