def digit(n, k):
    """Return the digit that is k from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    return (n // (10 ** k)) % 10


def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    return a + b + c - max(a, b, c) - min(a, b, c)  #直接相减是没想到的


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    # a=n    
    # b=n-1
    # if k==0 :
    #     return 1
    # while k-1:
    #     a=a*b
    #     b=b-1
    #     k=k-1
    # return a
    result = 1
    for _ in range(k):  # 循环k次
        result *= n     # 乘以当前的n
        n -= 1          # n减1，准备下一次乘法
    return result


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    # a=k
    # count = 0
    # while a <= n:  # 修改循环条件：使用<=确保n被包含
    #     print(a)
    #     count += 1
    #     a += k
    # return count
    count = n // k  # 计算范围内k的倍数的个数
    for num in range(k, k * (count + 1), k):  # 直接生成所有符合条件的数
        print(num)
    return count


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    total = 0  # 初始化变量，避免使用内置函数名
    while y > 0:
        total += y % 10
        y = y // 10
    return total

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    # while n!=0:
    #     if n//10!=0:
    #         if n%10==8 and (n//10)%10==8:
    #             return True
    #     n//=10
    # return False     
    while n > 0:
        if n % 10 == 8 and (n // 10) % 10 == 8:
            return True
        n //= 10
    return False
