# 60 Programming Fundamentals Problems — C++ Source Code

Each solution below is a separate program. Copy and compile one code block at a time.
These examples are compatible with C++17. Illustrative policy rules (grades, eligibility, tariffs) can be changed as needed.

## 1. Personal Introduction

File: `01_personal_introduction.cpp`

```cpp

#include <iostream>
#include <string>
using namespace std;

int main() {
    string name, department, semester, city;
    cout << "Enter your name: ";
    getline(cin, name);
    cout << "Enter your department: ";
    getline(cin, department);
    cout << "Enter your semester: ";
    getline(cin, semester);
    cout << "Enter your city: ";
    getline(cin, city);

    cout << "\n--- Student Introduction ---\n";
    cout << "Name: " << name << "\nDepartment: " << department
         << "\nSemester: " << semester << "\nCity: " << city << '\n';
    return 0;
}
```

## 2. Basic Arithmetic Calculator

File: `02_basic_arithmetic_calculator.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    double a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;

    cout << "Sum = " << a + b << '\n';
    cout << "Difference = " << a - b << '\n';
    cout << "Product = " << a * b << '\n';
    if (b != 0)
        cout << "Quotient = " << a / b << '\n';
    else
        cout << "Quotient is undefined because the second number is zero.\n";
    return 0;
}
```

## 3. Temperature Converter

File: `03_temperature_converter.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    double celsius, fahrenheit;
    cout << "Enter temperature in Celsius: ";
    cin >> celsius;
    fahrenheit = (9.0 / 5.0) * celsius + 32;
    cout << "Fahrenheit = " << fahrenheit << '\n';

    cout << "Enter temperature in Fahrenheit: ";
    cin >> fahrenheit;
    celsius = (fahrenheit - 32) * (5.0 / 9.0);
    cout << "Celsius = " << celsius << '\n';
    return 0;
}
```

## 4. Rectangle Calculator

File: `04_rectangle_calculator.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    double length, width;
    cout << "Enter length and width: ";
    cin >> length >> width;
    cout << "Area = " << length * width << '\n';
    cout << "Perimeter = " << 2 * (length + width) << '\n';
    return 0;
}
```

## 5. Shopping Bill

File: `05_shopping_bill.cpp`

```cpp

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double price1, price2, price3, discountPercent;
    int quantity1, quantity2, quantity3;

    cout << "Enter price and quantity for product 1: ";
    cin >> price1 >> quantity1;
    cout << "Enter price and quantity for product 2: ";
    cin >> price2 >> quantity2;
    cout << "Enter price and quantity for product 3: ";
    cin >> price3 >> quantity3;
    cout << "Enter discount percentage: ";
    cin >> discountPercent;

    double subtotal = price1 * quantity1 + price2 * quantity2 + price3 * quantity3;
    double discount = subtotal * discountPercent / 100.0;
    cout << fixed << setprecision(2);
    cout << "Subtotal = Rs. " << subtotal << '\n';
    cout << "Discount = Rs. " << discount << '\n';
    cout << "Final bill = Rs. " << subtotal - discount << '\n';
    return 0;
}
```

## 6. Student Marks Calculator

File: `06_student_marks_calculator.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    double marks, total = 0;
    const int SUBJECTS = 5;
    cout << "Enter marks for " << SUBJECTS << " subjects (each out of 100):\n";
    for (int i = 1; i <= SUBJECTS; ++i) {
        cout << "Subject " << i << ": ";
        cin >> marks;
        total += marks;
    }
    cout << "Total = " << total << " / " << SUBJECTS * 100 << '\n';
    cout << "Percentage = " << total / (SUBJECTS * 100.0) * 100 << "%\n";
    cout << "Average marks = " << total / SUBJECTS << '\n';
    return 0;
}
```

## 7. Time Converter

File: `07_time_converter.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    long long totalSeconds;
    cout << "Enter total seconds: ";
    cin >> totalSeconds;
    if (totalSeconds < 0) {
        cout << "Please enter a nonnegative number of seconds.\n";
        return 0;
    }
    long long hours = totalSeconds / 3600;
    long long minutes = (totalSeconds % 3600) / 60;
    long long seconds = totalSeconds % 60;
    cout << hours << " hour(s), " << minutes << " minute(s), "
         << seconds << " second(s)\n";
    return 0;
}
```

## 8. Distance Converter

File: `08_distance_converter.cpp`

```cpp

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double km;
    cout << "Enter distance in kilometres: ";
    cin >> km;
    cout << fixed << setprecision(3);
    cout << "Metres = " << km * 1000 << '\n';
    cout << "Centimetres = " << km * 100000 << '\n';
    cout << "Miles = " << km * 0.621371 << '\n';
    return 0;
}
```

## 9. Simple Interest Calculator

File: `09_simple_interest_calculator.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    double principal, rate, years;
    cout << "Enter principal, annual rate (%) and time (years): ";
    cin >> principal >> rate >> years;
    double interest = principal * rate * years / 100.0;
    cout << "Simple interest = " << interest << '\n';
    cout << "Total amount = " << principal + interest << '\n';
    return 0;
}
```

## 10. Electrical Power Calculator

File: `10_electrical_power_calculator.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    double voltage, current;
    cout << "Enter voltage (V) and current (A): ";
    cin >> voltage >> current;
    cout << "Power = " << voltage * current << " watts\n";
    if (current != 0)
        cout << "Resistance = " << voltage / current << " ohms\n";
    else
        cout << "Resistance V/I is undefined when current is zero.\n";
    return 0;
}
```

## 11. Positive, Negative or Zero

File: `11_positive,_negative_or_zero.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    double number;
    cout << "Enter a number: ";
    cin >> number;
    if (number > 0) cout << "Positive\n";
    else if (number < 0) cout << "Negative\n";
    else cout << "Zero\n";
    return 0;
}
```

## 12. Even or Odd

File: `12_even_or_odd.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    long long number;
    cout << "Enter an integer: ";
    cin >> number;
    if (number % 2 == 0) cout << "Even\n";
    else cout << "Odd\n";
    return 0;
}
```

## 13. Largest of Three Numbers

File: `13_largest_of_three_numbers.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    double a, b, c;
    cout << "Enter three numbers: ";
    cin >> a >> b >> c;
    if (a >= b && a >= c) cout << "Largest = " << a << '\n';
    else if (b >= a && b >= c) cout << "Largest = " << b << '\n';
    else cout << "Largest = " << c << '\n';
    return 0;
}
```

## 14. Divisibility Checker

File: `14_divisibility_checker.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter an integer: ";
    cin >> n;
    bool by3 = (n % 3 == 0);
    bool by5 = (n % 5 == 0);

    if (by3 && by5) cout << "Divisible by both 3 and 5\n";
    else if (by3) cout << "Divisible by 3 only\n";
    else if (by5) cout << "Divisible by 5 only\n";
    else cout << "Divisible by neither 3 nor 5\n";
    return 0;
}
```

## 15. Leap Year Checker

File: `15_leap_year_checker.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    int year;
    cout << "Enter a year: ";
    cin >> year;
    if (year <= 0) {
        cout << "Enter a positive year.\n";
    } else if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)) {
        cout << "Leap year\n";
    } else {
        cout << "Not a leap year\n";
    }
    return 0;
}
```

## 16. Grade Assignment

File: `16_grade_assignment.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    double marks;
    cout << "Enter marks (0 to 100): ";
    cin >> marks;
    if (marks < 0 || marks > 100) cout << "Invalid marks\n";
    else if (marks >= 80) cout << "Grade: A\n";
    else if (marks >= 70) cout << "Grade: B\n";
    else if (marks >= 60) cout << "Grade: C\n";
    else if (marks >= 50) cout << "Grade: D\n";
    else cout << "Grade: F\n";
    return 0;
}
```

## 17. Admission Eligibility

File: `17_admission_eligibility.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    double percentage, testScore;
    cout << "Enter previous-exam percentage and entry-test score (%): ";
    cin >> percentage >> testScore;
    // Illustrative thresholds; replace with the actual admission policy.
    if (percentage < 0 || percentage > 100 || testScore < 0 || testScore > 100) {
        cout << "Invalid score(s)\n";
    } else if (percentage >= 50 && testScore >= 50) {
        cout << "Meets the illustrative eligibility criteria\n";
    } else {
        cout << "Does not meet the illustrative eligibility criteria\n";
    }
    return 0;
}
```

## 18. Electricity Bill

File: `18_electricity_bill.cpp`

```cpp

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double units;
    const double FIXED_CHARGE = 150.0;
    cout << "Enter units consumed: ";
    cin >> units;
    if (units < 0) {
        cout << "Units cannot be negative.\n";
        return 0;
    }

    // Illustrative progressive slabs: first 100 at Rs. 10,
    // next 100 at Rs. 15, remaining units at Rs. 20.
    double bill = FIXED_CHARGE;
    if (units <= 100) bill += units * 10;
    else if (units <= 200) bill += 100 * 10 + (units - 100) * 15;
    else bill += 100 * 10 + 100 * 15 + (units - 200) * 20;

    cout << fixed << setprecision(2);
    cout << "Estimated bill = Rs. " << bill << '\n';
    return 0;
}
```

## 19. Triangle Classification

File: `19_triangle_classification.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    double a, b, c;
    cout << "Enter three side lengths: ";
    cin >> a >> b >> c;
    if (a <= 0 || b <= 0 || c <= 0 ||
        a + b <= c || a + c <= b || b + c <= a) {
        cout << "These sides do not form a triangle.\n";
    } else if (a == b && b == c) {
        cout << "Equilateral triangle\n";
    } else if (a == b || a == c || b == c) {
        cout << "Isosceles triangle\n";
    } else {
        cout << "Scalene triangle\n";
    }
    return 0;
}
```

## 20. ATM Withdrawal

File: `20_atm_withdrawal.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    double balance, amount;
    cout << "Enter account balance and withdrawal amount: ";
    cin >> balance >> amount;

    if (balance < 0 || amount <= 0) cout << "Invalid balance or amount\n";
    else if (amount > balance) cout << "Insufficient balance\n";
    else if (static_cast<long long>(amount) % 500 != 0 || amount != static_cast<long long>(amount))
        cout << "Amount must be a whole-number multiple of Rs. 500\n";
    else {
        balance -= amount;
        cout << "Withdrawal successful. Remaining balance = Rs. " << balance << '\n';
    }
    return 0;
}
```

## 21. Counting from 1 to N

File: `21_counting_from_1_to_n.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a positive integer N: ";
    cin >> n;
    if (n < 1) {
        cout << "N must be positive.\n";
        return 0;
    }
    for (int i = 1; i <= n; ++i) cout << i << ' ';
    cout << '\n';
    return 0;
}
```

## 22. Multiplication Table

File: `22_multiplication_table.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    for (int i = 1; i <= 10; ++i)
        cout << n << " x " << i << " = " << n * i << '\n';
    return 0;
}
```

## 23. Sum of First N Natural Numbers

File: `23_sum_of_first_n_natural_numbers.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    int n;
    long long sum = 0;
    cout << "Enter a positive integer N: ";
    cin >> n;
    if (n < 1) {
        cout << "N must be positive.\n";
        return 0;
    }
    for (int i = 1; i <= n; ++i) sum += i;
    cout << "Sum using loop = " << sum << '\n';
    cout << "Sum using formula = " << 1LL * n * (n + 1) / 2 << '\n';
    return 0;
}
```

## 24. Sum of Even Numbers

File: `24_sum_of_even_numbers.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    int n;
    long long sum = 0;
    cout << "Enter N: ";
    cin >> n;
    for (int i = 2; i <= n; i += 2) sum += i;
    cout << "Sum of even numbers from 1 to " << n << " = " << sum << '\n';
    return 0;
}
```

## 25. Factorial Calculator

File: `25_factorial_calculator.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    int n;
    unsigned long long factorial = 1;
    cout << "Enter a nonnegative integer (up to 20): ";
    cin >> n;
    if (n < 0 || n > 20) {
        cout << "Please enter a value from 0 to 20.\n";
        return 0;
    }
    for (int i = 2; i <= n; ++i) factorial *= i;
    cout << n << "! = " << factorial << '\n';
    return 0;
}
```

## 26. Count Digits

File: `26_count_digits.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    long long n;
    cout << "Enter a nonnegative integer: ";
    cin >> n;
    if (n < 0) {
        cout << "Please enter a nonnegative integer.\n";
        return 0;
    }
    int count = 0;
    do {
        ++count;
        n /= 10;
    } while (n > 0);
    cout << "Number of digits = " << count << '\n';
    return 0;
}
```

## 27. Reverse the Digits

File: `27_reverse_the_digits.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    long long n;
    cout << "Enter a nonnegative integer: ";
    cin >> n;
    if (n < 0) {
        cout << "Please enter a nonnegative integer.\n";
        return 0;
    }
    long long reversed = 0;
    do {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    } while (n > 0);
    cout << "Reversed number = " << reversed << '\n';
    return 0;
}
```

## 28. Sum of Digits

File: `28_sum_of_digits.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    long long n;
    cout << "Enter a nonnegative integer: ";
    cin >> n;
    if (n < 0) {
        cout << "Please enter a nonnegative integer.\n";
        return 0;
    }
    int sum = 0;
    do {
        sum += static_cast<int>(n % 10);
        n /= 10;
    } while (n > 0);
    cout << "Sum of digits = " << sum << '\n';
    return 0;
}
```

## 29. Prime Number Checker

File: `29_prime_number_checker.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter an integer: ";
    cin >> n;
    bool isPrime = (n >= 2);
    for (int divisor = 2; divisor <= n / divisor && isPrime; ++divisor) {
        if (n % divisor == 0) isPrime = false;
    }
    cout << n << (isPrime ? " is prime.\n" : " is not prime.\n");
    return 0;
}
```

## 30. Fibonacci Sequence

File: `30_fibonacci_sequence.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "How many Fibonacci terms? ";
    cin >> n;
    if (n < 1 || n > 90) {
        cout << "Enter a number from 1 to 90.\n";
        return 0;
    }
    unsigned long long a = 0, b = 1;
    for (int i = 0; i < n; ++i) {
        cout << a << ' ';
        unsigned long long next = a + b;
        a = b;
        b = next;
    }
    cout << '\n';
    return 0;
}
```

## 31. Number Guessing Game

File: `31_number_guessing_game.cpp`

```cpp

#include <iostream>
#include <random>
using namespace std;

int main() {
    random_device rd;
    mt19937 generator(rd());
    uniform_int_distribution<int> distribution(1, 100);
    int secret = distribution(generator), guess, attempts = 0;

    cout << "Guess the secret number from 1 to 100.\n";
    do {
        cout << "Your guess: ";
        cin >> guess;
        ++attempts;
        if (guess < secret) cout << "Too low.\n";
        else if (guess > secret) cout << "Too high.\n";
        else cout << "Correct! Attempts: " << attempts << '\n';
    } while (guess != secret);
    return 0;
}
```

## 32. Star and Number Patterns

File: `32_star_and_number_patterns.cpp`

```cpp

#include <iostream>
using namespace std;

int main() {
    int rows;
    cout << "Enter number of rows: ";
    cin >> rows;
    if (rows < 1 || rows > 50) {
        cout << "Enter a value from 1 to 50.\n";
        return 0;
    }

    cout << "Star pattern:\n";
    for (int i = 1; i <= rows; ++i) {
        for (int j = 1; j <= i; ++j) cout << "* ";
        cout << '\n';
    }

    cout << "Number pattern:\n";
    for (int i = 1; i <= rows; ++i) {
        for (int j = 1; j <= i; ++j) cout << j << ' ';
        cout << '\n';
    }
    return 0;
}
```

## 33. Square and Cube Functions

File: `33_square_and_cube_functions.cpp`

```cpp

#include <iostream>
using namespace std;

double square(double n) { return n * n; }
double cube(double n) { return n * n * n; }

int main() {
    double number;
    cout << "Enter a number: ";
    cin >> number;
    cout << "Square = " << square(number) << '\n';
    cout << "Cube = " << cube(number) << '\n';
    return 0;
}
```

## 34. Even/Odd Function

File: `34_even_odd_function.cpp`

```cpp

#include <iostream>
using namespace std;

bool isEven(int n) { return n % 2 == 0; }

int main() {
    int count, value;
    cout << "How many integers? ";
    cin >> count;
    for (int i = 1; i <= count; ++i) {
        cout << "Enter integer " << i << ": ";
        cin >> value;
        cout << value << (isEven(value) ? " is even.\n" : " is odd.\n");
    }
    return 0;
}
```

## 35. Maximum of Three

File: `35_maximum_of_three.cpp`

```cpp

#include <iostream>
using namespace std;

double largestOfThree(double a, double b, double c) {
    double largest = a;
    if (b > largest) largest = b;
    if (c > largest) largest = c;
    return largest;
}

int main() {
    double a, b, c;
    cout << "Enter three numbers: ";
    cin >> a >> b >> c;
    cout << "Largest = " << largestOfThree(a, b, c) << '\n';
    return 0;
}
```

## 36. Factorial Function

File: `36_factorial_function.cpp`

```cpp

#include <iostream>
using namespace std;

unsigned long long factorial(int n) {
    unsigned long long result = 1;
    for (int i = 2; i <= n; ++i) result *= i;
    return result;
}

int main() {
    int n;
    cout << "Enter an integer from 0 to 20: ";
    cin >> n;
    if (n < 0 || n > 20) cout << "Invalid input.\n";
    else cout << n << "! = " << factorial(n) << '\n';
    return 0;
}
```

## 37. Prime-Checking Function

File: `37_prime_checking_function.cpp`

```cpp

#include <iostream>
using namespace std;

bool isPrime(int n) {
    if (n < 2) return false;
    for (int d = 2; d <= n / d; ++d)
        if (n % d == 0) return false;
    return true;
}

int main() {
    int start, end;
    cout << "Enter start and end of range: ";
    cin >> start >> end;
    if (start > end) {
        cout << "Start must not exceed end.\n";
        return 0;
    }
    for (int n = start; n <= end; ++n)
        if (isPrime(n)) cout << n << ' ';
    cout << '\n';
    return 0;
}
```

## 38. Grade Calculator Functions

File: `38_grade_calculator_functions.cpp`

```cpp

#include <iostream>
using namespace std;

double percentage(double obtained, double maximum) {
    return obtained / maximum * 100.0;
}

char gradeFor(double p) {
    if (p >= 80) return 'A';
    if (p >= 70) return 'B';
    if (p >= 60) return 'C';
    if (p >= 50) return 'D';
    return 'F';
}

int main() {
    double obtained, maximum;
    cout << "Enter obtained and maximum marks: ";
    cin >> obtained >> maximum;
    if (maximum <= 0 || obtained < 0 || obtained > maximum) {
        cout << "Invalid marks.\n";
        return 0;
    }
    double p = percentage(obtained, maximum);
    cout << "Percentage = " << p << "%\n";
    cout << "Grade = " << gradeFor(p) << '\n';
    return 0;
}
```

## 39. Electrical Calculation Toolkit

File: `39_electrical_calculation_toolkit.cpp`

```cpp

#include <iostream>
using namespace std;

double power(double voltage, double current) { return voltage * current; }
double resistance(double voltage, double current) { return voltage / current; }
double energyKWh(double powerWatts, double hours) { return powerWatts * hours / 1000.0; }

int main() {
    double voltage, current, hours;
    cout << "Enter voltage (V), current (A), and operating hours: ";
    cin >> voltage >> current >> hours;
    if (current == 0 || hours < 0) {
        cout << "Current must be nonzero and hours must be nonnegative.\n";
        return 0;
    }
    double p = power(voltage, current);
    cout << "Power = " << p << " W\n";
    cout << "Resistance = " << resistance(voltage, current) << " ohms\n";
    cout << "Energy = " << energyKWh(p, hours) << " kWh\n";
    return 0;
}
```

## 40. Vowel, Consonant and Digit Counter

File: `40_vowel,_consonant_and_digit_counter.cpp`

```cpp

#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int countVowels(const string& text) {
    int count = 0;
    for (unsigned char ch : text) {
        char c = static_cast<char>(tolower(ch));
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') ++count;
    }
    return count;
}

int countConsonants(const string& text) {
    int count = 0;
    for (unsigned char ch : text)
        if (isalpha(ch) && string("aeiouAEIOU").find(static_cast<char>(ch)) == string::npos)
            ++count;
    return count;
}

int countDigits(const string& text) {
    int count = 0;
    for (unsigned char ch : text) if (isdigit(ch)) ++count;
    return count;
}

int main() {
    string text;
    cout << "Enter a line of text: ";
    getline(cin, text);
    cout << "Vowels = " << countVowels(text) << '\n';
    cout << "Consonants = " << countConsonants(text) << '\n';
    cout << "Digits = " << countDigits(text) << '\n';
    return 0;
}
```

## 41. Menu-Driven Calculator

File: `41_menu_driven_calculator.cpp`

```cpp

#include <iostream>
using namespace std;

double add(double a, double b) { return a + b; }
double subtract(double a, double b) { return a - b; }
double multiply(double a, double b) { return a * b; }
double divide(double a, double b) { return a / b; }

int main() {
    int choice;
    double a, b;
    do {
        cout << "\n1. Add  2. Subtract  3. Multiply  4. Divide  0. Exit\nChoice: ";
        cin >> choice;
        if (choice >= 1 && choice <= 4) {
            cout << "Enter two numbers: ";
            cin >> a >> b;
            switch (choice) {
                case 1: cout << add(a, b) << '\n'; break;
                case 2: cout << subtract(a, b) << '\n'; break;
                case 3: cout << multiply(a, b) << '\n'; break;
                case 4:
                    if (b == 0) cout << "Cannot divide by zero.\n";
                    else cout << divide(a, b) << '\n';
                    break;
            }
        } else if (choice != 0) {
            cout << "Invalid choice.\n";
        }
    } while (choice != 0);
    return 0;
}
```

## 42. Student Result Processing

File: `42_student_result_processing.cpp`

```cpp

#include <iostream>
using namespace std;

double totalMarks(double marks[], int size) {
    double total = 0;
    for (int i = 0; i < size; ++i) total += marks[i];
    return total;
}

double percentage(double total, double maximum) {
    return total / maximum * 100.0;
}

char gradeFor(double p) {
    if (p >= 80) return 'A';
    if (p >= 70) return 'B';
    if (p >= 60) return 'C';
    if (p >= 50) return 'D';
    return 'F';
}

int main() {
    const int SUBJECTS = 5;
    double marks[SUBJECTS];
    cout << "Enter marks in five subjects (each out of 100):\n";
    for (int i = 0; i < SUBJECTS; ++i) {
        cin >> marks[i];
        if (marks[i] < 0 || marks[i] > 100) {
            cout << "Invalid mark entered.\n";
            return 0;
        }
    }
    double total = totalMarks(marks, SUBJECTS);
    double p = percentage(total, SUBJECTS * 100.0);
    cout << "Total = " << total << '\n';
    cout << "Percentage = " << p << "%\n";
    cout << "Grade = " << gradeFor(p) << '\n';
    cout << "Result = " << (p >= 50 ? "Pass\n" : "Fail\n");
    return 0;
}
```

## 43. List Statistics

File: `43_list_statistics.cpp`

```cpp

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cout << "How many numbers? ";
    cin >> n;
    if (n <= 0) {
        cout << "Enter at least one number.\n";
        return 0;
    }
    vector<double> values(n);
    for (int i = 0; i < n; ++i) {
        cout << "Value " << i + 1 << ": ";
        cin >> values[i];
    }
    double sum = 0, minimum = values[0], maximum = values[0];
    for (double x : values) {
        sum += x;
        if (x < minimum) minimum = x;
        if (x > maximum) maximum = x;
    }
    cout << "Sum = " << sum << "\nCount = " << n
         << "\nAverage = " << sum / n << "\nMinimum = " << minimum
         << "\nMaximum = " << maximum << '\n';
    return 0;
}
```

## 44. Count Even and Odd Values

File: `44_count_even_and_odd_values.cpp`

```cpp

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, evenCount = 0, oddCount = 0, value;
    cout << "How many integers? ";
    cin >> n;
    if (n < 0) {
        cout << "Count cannot be negative.\n";
        return 0;
    }
    for (int i = 0; i < n; ++i) {
        cin >> value;
        if (value % 2 == 0) ++evenCount;
        else ++oddCount;
    }
    cout << "Even values = " << evenCount << "\nOdd values = " << oddCount << '\n';
    return 0;
}
```

## 45. Linear Search

File: `45_linear_search.cpp`

```cpp

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, target;
    cout << "Number of values: ";
    cin >> n;
    if (n < 0) return 0;
    vector<int> values(n);
    for (int i = 0; i < n; ++i) cin >> values[i];
    cout << "Value to search for: ";
    cin >> target;

    int foundIndex = -1;
    for (int i = 0; i < n; ++i) {
        if (values[i] == target) {
            foundIndex = i;
            break;
        }
    }
    if (foundIndex == -1) cout << "Value not found.\n";
    else cout << "Value found at zero-based index " << foundIndex << '\n';
    return 0;
}
```

## 46. Count Occurrences

File: `46_count_occurrences.cpp`

```cpp

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, target, count = 0;
    cout << "Number of values: ";
    cin >> n;
    if (n < 0) return 0;
    vector<int> values(n);
    for (int i = 0; i < n; ++i) cin >> values[i];
    cout << "Target value: ";
    cin >> target;
    for (int value : values) if (value == target) ++count;
    cout << "Occurrences = " << count << '\n';
    return 0;
}
```

## 47. Reverse a List

File: `47_reverse_a_list.cpp`

```cpp

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cout << "Number of values: ";
    cin >> n;
    if (n < 0) return 0;
    vector<int> values(n), reversed;
    for (int i = 0; i < n; ++i) cin >> values[i];
    for (int i = n - 1; i >= 0; --i) reversed.push_back(values[i]);

    cout << "Reversed list: ";
    for (int value : reversed) cout << value << ' ';
    cout << '\n';
    return 0;
}
```

## 48. Second-Largest Distinct Value

File: `48_second_largest_distinct_value.cpp`

```cpp

#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main() {
    int n;
    cout << "Number of values: ";
    cin >> n;
    if (n < 2) {
        cout << "At least two values are needed.\n";
        return 0;
    }
    int largest = INT_MIN, second = INT_MIN, value;
    bool hasLargest = false, hasSecond = false;
    for (int i = 0; i < n; ++i) {
        cin >> value;
        if (!hasLargest || value > largest) {
            if (hasLargest) {
                second = largest;
                hasSecond = true;
            }
            largest = value;
            hasLargest = true;
        } else if (value < largest && (!hasSecond || value > second)) {
            second = value;
            hasSecond = true;
        }
    }
    if (hasSecond) cout << "Second-largest distinct value = " << second << '\n';
    else cout << "No second-largest distinct value exists.\n";
    return 0;
}
```

## 49. Remove Duplicates

File: `49_remove_duplicates.cpp`

```cpp

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cout << "Number of values: ";
    cin >> n;
    if (n < 0) return 0;
    vector<int> values(n), uniqueValues;
    for (int i = 0; i < n; ++i) cin >> values[i];

    for (int value : values) {
        bool alreadyPresent = false;
        for (int existing : uniqueValues)
            if (existing == value) alreadyPresent = true;
        if (!alreadyPresent) uniqueValues.push_back(value);
    }

    cout << "List without duplicates: ";
    for (int value : uniqueValues) cout << value << ' ';
    cout << '\n';
    return 0;
}
```

## 50. Bubble Sort

File: `50_bubble_sort.cpp`

```cpp

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cout << "Number of values: ";
    cin >> n;
    if (n < 0) return 0;
    vector<int> values(n);
    for (int i = 0; i < n; ++i) cin >> values[i];

    for (int i = 0; i < n - 1; ++i) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; ++j) {
            if (values[j] > values[j + 1]) {
                int temp = values[j];
                values[j] = values[j + 1];
                values[j + 1] = temp;
                swapped = true;
            }
        }
        if (!swapped) break;
    }

    cout << "Sorted values: ";
    for (int value : values) cout << value << ' ';
    cout << '\n';
    return 0;
}
```

## 51. Class Marks Analysis

File: `51_class_marks_analysis.cpp`

```cpp

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, passCount = 0;
    cout << "Number of students: ";
    cin >> n;
    if (n <= 0) {
        cout << "Enter at least one student.\n";
        return 0;
    }
    vector<double> marks(n);
    double total = 0, highest = -1, lowest = 101;
    for (int i = 0; i < n; ++i) {
        cout << "Marks for student " << i + 1 << " (0-100): ";
        cin >> marks[i];
        if (marks[i] < 0 || marks[i] > 100) {
            cout << "Invalid marks.\n";
            return 0;
        }
        total += marks[i];
        if (marks[i] > highest) highest = marks[i];
        if (marks[i] < lowest) lowest = marks[i];
        if (marks[i] >= 50) ++passCount;
    }
    cout << "Class average = " << total / n << '\n';
    cout << "Highest = " << highest << "\nLowest = " << lowest
         << "\nStudents passed (50 or above) = " << passCount << '\n';
    return 0;
}
```

## 52. Word Frequency Counter

File: `52_word_frequency_counter.cpp`

```cpp

#include <iostream>
#include <sstream>
#include <map>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string line, word;
    cout << "Enter a sentence: ";
    getline(cin, line);

    // Convert to lowercase and replace basic punctuation with spaces.
    for (char &ch : line) {
        unsigned char u = static_cast<unsigned char>(ch);
        if (ispunct(u)) ch = ' ';
        else ch = static_cast<char>(tolower(u));
    }

    map<string, int> frequency;
    stringstream input(line);
    while (input >> word) ++frequency[word];

    for (const auto &entry : frequency)
        cout << entry.first << ": " << entry.second << '\n';
    return 0;
}
```

## 53. Student Record System

File: `53_student_record_system.cpp`

```cpp

#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

struct Student {
    string name;
    double marks;
};

int main() {
    vector<Student> students;
    int choice;
    do {
        cout << "\n1. Add student  2. Display records  3. Highest mark  0. Exit\nChoice: ";
        cin >> choice;
        if (choice == 1) {
            Student s;
            cout << "Enter student name: ";
            getline(cin >> ws, s.name);
            cout << "Enter percentage (0-100): ";
            cin >> s.marks;
            if (s.marks < 0 || s.marks > 100) cout << "Invalid percentage.\n";
            else students.push_back(s);
        } else if (choice == 2) {
            if (students.empty()) cout << "No records available.\n";
            for (const Student &s : students)
                cout << s.name << " - " << s.marks << "%\n";
        } else if (choice == 3) {
            if (students.empty()) cout << "No records available.\n";
            else {
                Student best = students[0];
                for (const Student &s : students)
                    if (s.marks > best.marks) best = s;
                cout << "Highest scorer: " << best.name << " (" << best.marks << "%)\n";
            }
        } else if (choice != 0) cout << "Invalid choice.\n";
    } while (choice != 0);
    return 0;
}
```

## 54. Mini Banking System

File: `54_mini_banking_system.cpp`

```cpp

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double balance;
    cout << "Enter opening balance: ";
    cin >> balance;
    if (balance < 0) {
        cout << "Balance cannot be negative.\n";
        return 0;
    }

    int choice;
    do {
        cout << "\n1. Deposit  2. Withdraw  3. Check balance  0. Exit\nChoice: ";
        cin >> choice;
        if (choice == 1) {
            double amount;
            cout << "Deposit amount: ";
            cin >> amount;
            if (amount <= 0) cout << "Amount must be positive.\n";
            else balance += amount;
        } else if (choice == 2) {
            double amount;
            cout << "Withdrawal amount: ";
            cin >> amount;
            if (amount <= 0) cout << "Amount must be positive.\n";
            else if (amount > balance) cout << "Insufficient funds.\n";
            else balance -= amount;
        } else if (choice == 3) {
            cout << fixed << setprecision(2) << "Balance = Rs. " << balance << '\n';
        } else if (choice != 0) cout << "Invalid choice.\n";
    } while (choice != 0);

    cout << "Final balance = Rs. " << fixed << setprecision(2) << balance << '\n';
    return 0;
}
```

## 55. Inventory and Shopping System

File: `55_inventory_and_shopping_system.cpp`

```cpp

#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

struct Product {
    string name;
    double price;
    int quantity;
};

int main() {
    vector<Product> products = {
        {"Notebook", 120.0, 20},
        {"Pen", 40.0, 50},
        {"USB Drive", 900.0, 10}
    };
    double bill = 0;
    int choice, quantity;

    do {
        cout << "\nAvailable products:\n";
        for (int i = 0; i < static_cast<int>(products.size()); ++i)
            cout << i + 1 << ". " << products[i].name << " - Rs. "
                 << products[i].price << " (stock: " << products[i].quantity << ")\n";
        cout << "0. Checkout\nSelect product: ";
        cin >> choice;

        if (choice == 0) break;
        if (choice < 1 || choice > static_cast<int>(products.size())) {
            cout << "Invalid selection.\n";
            continue;
        }
        cout << "Quantity: ";
        cin >> quantity;
        Product &p = products[choice - 1];
        if (quantity <= 0) cout << "Quantity must be positive.\n";
        else if (quantity > p.quantity) cout << "Insufficient stock.\n";
        else {
            bill += p.price * quantity;
            p.quantity -= quantity;
            cout << "Added to bill.\n";
        }
    } while (true);

    cout << fixed << setprecision(2) << "Final bill = Rs. " << bill << '\n';
    return 0;
}
```

## 56. Electricity Consumption Analyzer

File: `56_electricity_consumption_analyzer.cpp`

```cpp

#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    const int DAYS = 30;
    vector<double> units(DAYS);
    double total = 0, highest = -1;
    int highestDay = 0;

    cout << "Enter electricity consumption for 30 days (kWh):\n";
    for (int i = 0; i < DAYS; ++i) {
        cout << "Day " << i + 1 << ": ";
        cin >> units[i];
        if (units[i] < 0) {
            cout << "Consumption cannot be negative.\n";
            return 0;
        }
        total += units[i];
        if (units[i] > highest) {
            highest = units[i];
            highestDay = i + 1;
        }
    }

    // Illustrative flat tariff; change to match the required tariff.
    const double RATE = 20.0;
    cout << fixed << setprecision(2);
    cout << "Total consumption = " << total << " kWh\n";
    cout << "Daily average = " << total / DAYS << " kWh\n";
    cout << "Highest consumption = " << highest << " kWh on day " << highestDay << '\n';
    cout << "Estimated bill at Rs. " << RATE << " per kWh = Rs. " << total * RATE << '\n';
    return 0;
}
```

## 57. Quiz Application

File: `57_quiz_application.cpp`

```cpp

#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Question {
    string prompt;
    string options[4];
    char correct;
};

int main() {
    vector<Question> quiz = {
        {"Which operator gives the remainder?", {"A) /", "B) %", "C) *", "D) + "}, 'B'},
        {"Which type stores true or false?", {"A) int", "B) char", "C) bool", "D) string"}, 'C'},
        {"Which loop checks its condition before each iteration?", {"A) while", "B) do-while", "C) switch", "D) if"}, 'A'}
    };
    int score = 0;
    for (const Question &q : quiz) {
        cout << "\n" << q.prompt << '\n';
        for (const string &option : q.options) cout << option << '\n';
        char answer;
        cout << "Your answer (A-D): ";
        cin >> answer;
        if (toupper(static_cast<unsigned char>(answer)) == q.correct) {
            ++score;
            cout << "Correct!\n";
        } else {
            cout << "Incorrect. Correct answer: " << q.correct << '\n';
        }
    }
    double percentage = 100.0 * score / quiz.size();
    cout << "\nScore = " << score << "/" << quiz.size()
         << "\nPercentage = " << percentage << "%\n";
    return 0;
}
```

## 58. Text Analyzer

File: `58_text_analyzer.cpp`

```cpp

#include <iostream>
#include <sstream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string text;
    cout << "Enter a paragraph on one line: ";
    getline(cin, text);

    int vowels = 0, digits = 0, sentences = 0;
    for (unsigned char ch : text) {
        char c = static_cast<char>(tolower(ch));
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') ++vowels;
        if (isdigit(ch)) ++digits;
        if (ch == '.' || ch == '!' || ch == '?') ++sentences;
    }

    string word;
    int words = 0;
    stringstream input(text);
    while (input >> word) ++words;

    cout << "Characters (including spaces) = " << text.size() << '\n';
    cout << "Words = " << words << '\n';
    cout << "Sentence-ending punctuation marks = " << sentences << '\n';
    cout << "Vowels = " << vowels << '\n';
    cout << "Digits = " << digits << '\n';
    return 0;
}
```

## 59. Expense Tracker

File: `59_expense_tracker.cpp`

```cpp

#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

struct Expense {
    string category;
    string description;
    double amount;
};

int main() {
    vector<Expense> expenses;
    int n;
    cout << "How many expenses will you enter? ";
    cin >> n;
    if (n < 0) return 0;

    for (int i = 0; i < n; ++i) {
        Expense e;
        cout << "Category (food/transport/books/utilities/other): ";
        cin >> e.category;
        cout << "Short description: ";
        getline(cin >> ws, e.description);
        cout << "Amount (Rs.): ";
        cin >> e.amount;
        if (e.amount < 0) {
            cout << "Amount cannot be negative.\n";
            return 0;
        }
        expenses.push_back(e);
    }

    double total = 0, largest = -1;
    int largestIndex = -1;
    for (int i = 0; i < static_cast<int>(expenses.size()); ++i) {
        total += expenses[i].amount;
        if (expenses[i].amount > largest) {
            largest = expenses[i].amount;
            largestIndex = i;
        }
    }

    cout << fixed << setprecision(2);
    cout << "\nTotal expenditure = Rs. " << total << '\n';
    cout << "Category totals:\n";
    vector<string> categories = {"food", "transport", "books", "utilities", "other"};
    for (const string &category : categories) {
        double subtotal = 0;
        for (const Expense &e : expenses)
            if (e.category == category) subtotal += e.amount;
        cout << category << ": Rs. " << subtotal << '\n';
    }
    if (largestIndex >= 0)
        cout << "Largest expense: " << expenses[largestIndex].description
             << " (Rs. " << largest << ")\n";
    return 0;
}
```

## 60. Mini Examination Management System

File: `60_mini_examination_management_system.cpp`

```cpp

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

struct Student {
    string name;
    vector<double> marks;
    double total = 0;
    double percentage = 0;
    char grade = 'F';
    bool passed = false;
};

char gradeFor(double p) {
    if (p >= 80) return 'A';
    if (p >= 70) return 'B';
    if (p >= 60) return 'C';
    if (p >= 50) return 'D';
    return 'F';
}

int main() {
    int n, subjects;
    cout << "Number of students: ";
    cin >> n;
    cout << "Number of subjects: ";
    cin >> subjects;
    if (n <= 0 || subjects <= 0) {
        cout << "Both counts must be positive.\n";
        return 0;
    }

    vector<Student> students(n);
    for (int i = 0; i < n; ++i) {
        cout << "\nStudent " << i + 1 << " name: ";
        getline(cin >> ws, students[i].name);
        students[i].marks.resize(subjects);
        for (int j = 0; j < subjects; ++j) {
            cout << "Subject " << j + 1 << " marks (0-100): ";
            cin >> students[i].marks[j];
            if (students[i].marks[j] < 0 || students[i].marks[j] > 100) {
                cout << "Invalid marks.\n";
                return 0;
            }
            students[i].total += students[i].marks[j];
        }
        students[i].percentage = students[i].total / subjects;
        students[i].grade = gradeFor(students[i].percentage);
        students[i].passed = students[i].percentage >= 50;
    }

    sort(students.begin(), students.end(),
         [](const Student &a, const Student &b) { return a.total > b.total; });

    cout << "\nRanked class results:\n";
    cout << fixed << setprecision(2);
    for (int i = 0; i < n; ++i) {
        cout << i + 1 << ". " << students[i].name
             << " | Total: " << students[i].total << "/" << subjects * 100
             << " | Percentage: " << students[i].percentage << "%"
             << " | Grade: " << students[i].grade
             << " | " << (students[i].passed ? "Pass" : "Fail") << '\n';
    }
    return 0;
}
```
