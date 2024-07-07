from typing import Callable, Generator
import re

text1 = 100
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(str_text: str) -> Generator[str, None, None]:
    '''
    The function picks numbers (as a strings) 
    from a string(argument). And yields numbers as
    separated strings.
    '''
        
    # alternative version in two lines
    # pattern = re.compile(r'\d+.{1}\d+')
    # digits = re.findall(pattern, str(str_text))

    text_list = str(str_text).split() # instead of caching AttributeError
                                      # used str(), so we can send int to the function
    pattern = re.compile(r'\d+')
    digits = [x for x in text_list if pattern.match(x)]
    
    for n in digits:
        yield n

def sum_profit(str_text: str, func: Callable) -> float:
    '''
    This function takes a str, processes it by the 
    given function, and returns sum of numbers from the string.
    The argument function has to return or 
    yield numnbers as any type (str, int, float, tuple, etc.).
    '''
    total_sum = 0
    try:
        for n in func(str_text):
            total_sum += float(n)
    except AttributeError:
        print('The atribute function retorns wrong data!')
    return total_sum


if __name__ == '__main__':
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

    total_income = sum_profit(text1, generator_numbers)
    print(f"Загальний дохід: {total_income}")
