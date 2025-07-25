# 사용자로부터 입력받은 숫자들의 평균을 계산하는 파이썬 함수 작성하기

def compute_average(numbers):
    """숫자 리스트를 받아 평균을 계산합니다.

    Args:
        numbers (list[float]): 평균을 계산할 숫자들의 리스트.

    Returns:
        float: 계산된 평균값.

    Raises:
        ZeroDivisionError: 비어 있는 리스트가 입력될 경우.
    """
    if not numbers:
        raise ZeroDivisionError("평균을 계산할 숫자가 없습니다.")
    return sum(numbers) / len(numbers)

def calculate_average_from_input():
    """사용자 입력을 받아 평균을 계산하고 결과를 출력합니다."""
    numbers = input("숫자들을 공백으로 구분하여 입력하세요: ")
    try:
        num_list = [float(num) for num in numbers.split()]
        avg = compute_average(num_list)
        print(f"입력한 숫자들의 평균은 {avg}입니다.")
        return avg
    except ValueError:
        print("오류: 숫자만 입력해주세요. 문자가 포함되어 있습니다.")
        return None
    except ZeroDivisionError:
        print("오류: 입력된 숫자가 없습니다.")
        return None

# 함수 실행 예시
if __name__ == "__main__":
    calculate_average_from_input()