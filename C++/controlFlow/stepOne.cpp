#include <iostream>
#include <ostream>

int blockIf() {
  int age = 18;

  if (age >= 18) {
    std::cout << "You can vote!" << std::endl;
  } else {
    std::cout << "Too young to vote." << std::endl;
  }

  return 0;
  /*
  The program checks the condition inside if. If it's true, the first block
  runs. If it's fake, the esle block runs.
  */
}

int blockSwitch() {
  int day = 3;

  switch (day) {
  case 1:
    std::cout << "Monday";
    break;
  case 2:
    std::cout << "Tuesday";
    break;
  case 3:
    std::cout << "Wednesday";
    break;
  default:
    std::cout << "Invalid day";
  }

  /*
  Use switch when you have multiple possible outcomes for one variable. It’s
  often cleaner than using many if-else statements.
  */
  return 0;
}

int main() {
  int x = 5;

  if (x == 5) {
    goto label;

    std::cout << "This line will be skipped." << std::endl;
  }

label:
  std::cout << "Jumped to label!" << std::endl;

  return 0;

  /*
   The goto statement allows you to jump directly to another part of your code.
  */
}
