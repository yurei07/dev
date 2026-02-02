#include <iostream>
int a = 5;
int b = 5;

// ***** Arithmetic Operation in C++ *****

int sum = a + b; // it adds two numbers together

int difference = a - b; // it substracts one number from other

int product = a * b; // it multiplies two numbers together

int quotient = a / b;               // integer division
int quitient = float(a) / float(b); // floating-point division

int remainder = a % b; // it calculates the remainder of an integer division

int x = 5;
int y = ++x; // x = 6 y = 6
int z = x++; // x = 7 z = 6
/*
  It increments the value of a variable by 1.
  There are two ways to use this operator: prefix (++x)
  and postfix (x++). Prefix increments the value before returning it,
  whereas postfix returns the value first and then increments it.
*/

int y1 = --x; // x = 4, y1 = 4
int z1 = x--; // x = 3, z1 = 4
/*
 It decrements the value of a variable by 1. It can also be used in prefix (--x)
 and postfix (x--) forms.
*/

// ***** Logical Operators in C++ *****

int operatorAnd() {
  if (a > 0 && b > 0) {
    std::cout << "Both values are positive.\n";
  }
  /*
    AND Operator (&&) The AND operator checks if
    both the operands/conditions are true, then the expression is true.
    If any one of the conditions is false, the whole expression will be false.
  */
  return 0;
}

int operatorOr() {
  if (a > 0 || b > 0) {
    std::cout << "At least one value is positive.\n";
  }
  /*
  OR Operator (||) The OR operator checks if either of
  the operands/conditions are true, then the expression is true.
  If both the conditions are false, it will be false.
  */
  return 0;
}

int operatorNot() {
  if (!(a < 0)) {
    std::cout << "The value is not negative.\n";
  }
  /*
  NOT Operator (!) The NOT operator reverses the result
  of the condition/expression it is applied on. If the condition is true,
  the NOT operator will make it false and vice versa.
  */
  return 0;
}

// ***** Bitwise Operators in C++ *****

int result = 5 & 3; // result will be 1 (0000 0101 & 0000 0011 = 0000 0001)

int result0 = 5 | 3; // result will be 7 (0000 0101 | 0000 0011 = 0000 0111)

int result1 = 5 ^ 3; // result will be 6 (0000 0101 ^ 0000 0011 = 0000 0110)

int result2 = ~5; // result will be -6 (1111 1010)

int result3 = 5 << 1; // result will be 10 (0000 0101 << 1 = 0000 1010)

int result4 = 5 >> 1; // result will be 2 (0000 0101 >> 1 = 0000 0010)
