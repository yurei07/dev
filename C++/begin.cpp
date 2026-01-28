#include <clocale>
#include <iostream> // подключение какой либо дерективы

int main() { // функция в c++
  int num = 45;  // делаем переменнуй именно для полных числ
  std::cout << num << std::endl; // выводим данное число и выводим в другую строку благодоря endl
  // setlocale(LC_ALL,"RU,DE");  // это кодировка для языков такие как русский или немецки и другие

  // std::cout << "Hello World!" << std::endl;
  // std::cout << "Hallo Welt!" << std::endl;
  // std::cout << "Привет Мир!";
  

  // переменные 
  int a,b;
  std::cout << "Input a number of a: ";
  std::cin >> a; // выводим значение 

  
  std::cout << "Input a number of b: ";
  std::cin >> b;

  std::cout << "A: " << a << ". B: " << b;

  // Тиы данных
  int num = 2 // хранит тоже цифра и может до считаьб 
  float num3 = 3.213123; // хранит значение с цыфрами и точками
  double num4 = 1231.41; // так же хранит цыфри с точкой
  short num1 = 7 // хранит цифры от -32к до 32к
  char sym = "&" // для всх символов

















  return 0;
}
