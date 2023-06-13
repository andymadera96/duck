Test-driven development (TDD) 

![image of tdd](https://developer.ibm.com/developer/default/articles/5-steps-of-test-driven-development/images/tdd-red-green-refactoring-v3.png)

TDD is a software development practice that emphasizes writing automated tests before writing the actual code. The TDD process typically follows a sequence of steps: 

1. Write a test: The developer writes a test case that describes the desired behavior of a specific piece of code. The test is usually written in a testing framework or library that provides assertions and test fixtures.

2. Run the test: The developer runs the test and, since the code being tested doesn't exist yet, the test will fail initially.

3. Write the code: The developer writes the minimal amount of code necessary to make the test pass. This code could be a function, method, or class, depending on the level of granularity being tested.

4. Run all tests: After writing the code, the developer runs all the tests, including the new one just created. This step ensures that the new code hasn't broken any existing functionality.

5. Refactor the code: If necessary, the developer refactors the code to improve its design and maintainability. Refactoring is done with the safety net of the existing tests, which helps ensure that any changes made haven't introduced bugs.

6. Repeat: The developer repeats the cycle by writing another test for the next desired feature or functionality and goes through the process of making it pass.

The main idea behind TDD is to guide the development process through a series of small, incremental steps driven by tests. By writing tests first, developers can better understand the requirements, design the code to meet those requirements, and ensure that the code functions as intended. TDD can help improve code quality, reduce bugs, and provide a safety net for making changes or adding new features in the future.


To learn more: https://developer.ibm.com/articles/5-steps-of-test-driven-development/

How to Run Tests in Python: 

Command: python3 -m unittest test.models.ducks_test

Ex: Terminal Use
-----------------------start of terminal-----------------------
(venv) renato@Renatos-MacBook-Pro duck % python3 -m unittest test.models.ducks_test
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
-----------------------end of terminal-------------------------

