# CMPS 2200  Recitation 02

**Name (Team Member 1):**_________________________  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

Using the Master Theorem, for f(n) = 1, the work is mainly due to the recursive calls, leading to W(n) being Theta of n to the power of log base b of a. When f(n) = log n, the work might fit Case 2 of the Master Theorem, indicating W(n) is Theta of n to the power of log base b of a times log n if a equals b to the power of log base b of a. For f(n) = n, the situation aligns with a scenario where the non-recursive work has a significant impact, guiding the overall work computation.

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

When f(n) = n^c, the asymptotic behavior of W(n) depends on the relationship between c and log base b of a. If c is less than log base b of a, W(n) follows Theta of n to the power of log base b of a, dominated by the recursive structure. If c is greater than log base b of a, then W(n) is Theta of n^c, dominated by the work at each level, and if c equals log base b of a, W(n) is Theta of n^c times log n, indicating a balance between the work of recursive calls and work at each level.

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

For a recursive algorithm with W(n) represented as its running time, if we always had a processors available, the span of the algorithm would primarily depend on the depth of the recursion. Implementing span_calc allows us to compute the empirical span, and when comparing spans, the span for f(n) = 1, log n, and n would generally show that the span is minimized when parallelism is maximized, typically aligning with the logarithm of the depth of the recursion tree. Deriving and comparing the asymptotic expressions for these spans confirms that parallel execution significantly reduces the span, especially for cases where work at each level is not the dominant factor.
