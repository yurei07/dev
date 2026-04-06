/*
A function is a group of statements that perform a specific task, organized as a
separate unit in a program. Functions help in breaking the code into smaller,
manageable, and reusable blocks.
*/

#include <iostream>

int function_name(int) {
  // function body
}

/*
* return_type(int): Data type of the output produced by the function. It can be
void, indicating that the function doesn't return any value.

* function_name: Name given to the function, following C++ naming conventions.

* parameter list(int): List of input parameters/arguments that are needed to
perform the task. It is optional, you can leave it blank when no parameters are
needed.

*/

// **************** Function Prototypes **************** //

int multiplyNumbers(int x, int y);

int main() {
  int num1 = 3, num2 = 7;
  int result = multiplyNumbers(num1, num2); // Calling the function
  std::cout << "The product is: " << result << '\n';
  return 0;
}

// Function definition
int multiplyNumbers(int x, int y) {
  int product = x * y;
  return product;
}
