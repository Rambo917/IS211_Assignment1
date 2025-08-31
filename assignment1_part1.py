class ListDivideException(Exception): pass

def list_divide(numbers, divide=2):
    return sum(1 for number in numbers if number % divide == 0)

def test_list_divide():
    if list_divide([1,2,3,4,5]) != 2:
        raise ListDivideException()
    if list_divide([2,4,6,8,10]) != 5:
        raise ListDivideException()
    if list_divide([30, 54, 63,98, 100], divide=10) != 2:
        raise ListDivideException()
    if list_divide([]) != 0:
        raise ListDivideException()
    if list_divide([1,2,3,4,5], 1) != 5:
        raise ListDivideException()

if __name__ == "__main__":
    test_list_divide()

   git commit -m "Add assignment1_part1.py with list_divide and test cases"