from main import *

def test_simple_work():
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(16, 2, 2) == 80  
  assert simple_work_calc(27, 3, 3) == 108  
  assert simple_work_calc(8, 2, 2) == 32
 

def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(10, 2, 2,lambda n: n/2) == 22.0
  assert work_calc(10, 2, 2,lambda n: 1/n) == 10.5
  assert work_calc(10, 2, 2,lambda n: n*2) == 64



def test_compare_work():
  # Define work functions directly
  # Work function 1: a = 2, b = 2, f(n) = n
  work_fn1 = lambda n: work_calc(n, 2, 2, lambda x: x)
  # Work function 2: a = 2, b = 2, f(n) = n^2
  work_fn2 = lambda n: work_calc(n, 2, 2, lambda x: x**2)

  # Use the provided lines for comparison and printing results
  res = compare_work(work_fn1, work_fn2)
  print(res)

	
def test_compare_span():
  # Define span functions directly for comparison

  # Span function 1: a = 2, b = 2, f(n) = n
  span_fn1 = lambda n: span_calc(n, 2, 2, lambda x: x)

  # Span function 2: a = 2, b = 2, f(n) = log(n)
  span_fn2 = lambda n: span_calc(n, 2, 2, lambda x: math.log(x) if x > 0 else 0)

  # Use the provided structure for comparison and printing results
  res = compare_span(span_fn1, span_fn2)
  print_results(res)
