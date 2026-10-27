# 60 Programming Fundamentals Problems for First-Semester BS Students

As a computer science faculty member teaching freshly enrolled BS students, I would design these problems to develop computational thinking, algorithmic reasoning, problem decomposition, and coding confidence rather than merely practising programming syntax.

Students entering from Intermediate Pre-Engineering, ICS, and three-year Associate Diplomas in Electrical or Electronic Engineering have different strengths. Some may be comfortable with mathematics and logic, while others may have practical experience with measurements, electrical quantities, and technical calculations but limited programming exposure.

The problems below use familiar everyday situations, introductory mathematics, and technical applications. They progress from simple input/output to problem-solving with functions and collections.

## Suggested progression

## 01

Foundations and sequence

Problems 1–10 · Input, output, variables, expressions and type conversion

## 02

Selection and decision-making

Problems 11–20 · Boolean expressions, if/elif/else and nested decisions

## 03

Iteration and repetition

Problems 21–32 · for loops, while loops, counters and accumulators

## 04

Functions and decomposition

Problems 33–42 · Parameters, return values and reusable solutions

## 05

Lists and basic data processing

Problems 43–52 · Collections, traversal, searching and aggregation

## 06

Integrated problem-solving

Problems 53–60 · Combining multiple programming concepts

The sequence assumes Python as the teaching language, but the underlying problems are language-independent and can also be solved in C, C++, Java, or Dart.

## 1. Foundations: Input, Output and Expressions

Problems 1–10 · Learn to translate a statement into inputs, processing and outputs.

## 1

Personal Introduction

Ask the user for their name, department, semester and city. Display the information as a properly formatted introduction.

Concepts: input, output, variables, strings.

## 2

Basic Arithmetic Calculator

Input two numbers and display their sum, difference, product and quotient. Assume the second number is nonzero.

Concepts: arithmetic operators, numeric input, type conversion.

## 3

Temperature Converter

Convert a temperature from Celsius to Fahrenheit using \\(F = \frac{9}{5}C + 32\\). Extend the program to support conversion in the opposite direction.

Concepts: formulas, floating-point arithmetic, assignment.

## 4

Rectangle Calculator

Input length and width. Calculate the area and perimeter of a rectangle.

Concepts: formulas, variables and operator precedence.

## 5

Shopping Bill

Input the price and quantity of three products. Calculate the subtotal, discount amount and final bill using a specified discount percentage.

Concepts: arithmetic, percentages and multiple inputs.

## 6

Student Marks Calculator

Input marks in five subjects. Calculate total marks, percentage and average marks, assuming each subject has equal maximum marks.

Concepts: aggregation, division and percentages.

## 7

Time Converter

Input a total number of seconds and convert it into hours, minutes and remaining seconds.

Concepts: integer division (//) and remainder (%).

## 8

Distance Converter

Input a distance in kilometres and convert it into metres, centimetres and miles using specified conversion factors.

Concepts: arithmetic expressions, constants and units.

## 9

Simple Interest Calculator

Input principal, annual interest rate and time in years. Calculate simple interest and the total amount payable using \\(I = \frac{PRT}{100}\\).

Concepts: formulas, percentages and financial calculations.

## 10

Electrical Power Calculator

Input voltage and current. Calculate electrical power using \\(P = VI\\). Also calculate resistance using \\(R = V/I\\), assuming current is nonzero.

Concepts: formula implementation and technical applications.

## 2. Selection: Conditions and Decisions

Problems 11–20 · Decide which action to perform based on input values.

## 11

Positive, Negative or Zero

Input a number and determine whether it is positive, negative or zero.

Concepts: if/elif/else and relational operators.

## 12

Even or Odd

Input an integer and determine whether it is even or odd using the remainder operator.

Concepts: modulo, equality and Boolean conditions.

## 13

Largest of Three Numbers

Input three numbers and display the largest. Handle cases where two or all three numbers are equal.

Concepts: compound conditions, comparisons and ties.

## 14

Divisibility Checker

Input an integer and determine whether it is divisible by both 3 and 5, by only one of them, or by neither.

Concepts: logical AND, OR and remainder.

## 15

Leap Year Checker

Determine whether an input year is a leap year according to the Gregorian calendar rules.

Concepts: nested conditions and compound Boolean expressions.

## 16

Grade Assignment

Input marks from 0 to 100 and assign grades using a provided grading scale. Reject marks outside the valid range.

Concepts: ordered conditions, ranges and input validation.

## 17

Admission Eligibility

Input a candidate's marks percentage and entry-test score. Apply given eligibility rules using minimum thresholds for both values.

Concepts: logical operators and multiple criteria.

## 18

Electricity Bill

Calculate a household electricity bill using specified consumption slabs, rates and a fixed charge. Define clearly whether the rates are slab-wise or flat-rate.

Concepts: nested selection, ranges and arithmetic.

## 19

Triangle Classification

Input three side lengths. First check whether they can form a triangle; if valid, determine whether it is equilateral, isosceles or scalene.

Concepts: compound conditions, validation and nested decisions.

## 20

ATM Withdrawal

Input an account balance and withdrawal amount. Approve the transaction only if the amount is positive, does not exceed the balance, and is a multiple of a specified denomination such as Rs. 500.

Concepts: compound Boolean expressions, validation and decision logic.

## 3. Iteration: Loops and Repeated Computation

Problems 21–32 · Introduce counting, accumulation, repetition and pattern generation.

## 21

Counting from 1 to N

Input a positive integer N and display all integers from 1 through N.

Concepts: for loops, ranges and loop boundaries.

## 22

Multiplication Table

Input a number and display its multiplication table from 1 to 10.

Concepts: iteration, expressions and formatted output.

## 23

Sum of First N Natural Numbers

Input N and calculate the sum of the integers from 1 to N using a loop. Later, compare the result with the formula \\(N(N+1)/2\\).

Concepts: accumulators and algorithm verification.

## 24

Sum of Even Numbers

Calculate the sum of all even numbers between 1 and N.

Concepts: loops, conditions and accumulation.

## 25

Factorial Calculator

Calculate the factorial of a nonnegative integer N, where \\(0! = 1\\).

Concepts: iterative multiplication, initial values and special cases.

## 26

Count Digits

Input a nonnegative integer and count its digits. Treat zero as a one-digit number.

Concepts: while loops, integer division and edge cases.

## 27

Reverse the Digits

Input a nonnegative integer and display its digits in reverse order. For example, 472 becomes 274.

Concepts: loops, modulo and integer division.

## 28

Sum of Digits

Calculate the sum of the digits of an integer. For example, 472 produces 13.

Concepts: digit extraction, repeated processing and accumulators.

## 29

Prime Number Checker

Determine whether an integer greater than or equal to 2 is prime by testing possible divisors up to its square root.

Concepts: loops, divisibility and early termination.

## 30

Fibonacci Sequence

Display the first N terms of the Fibonacci sequence, beginning with 0 and 1.

Concepts: updating multiple variables and tracking state.

## 31

Number Guessing Game

Generate or specify a secret number. Allow the user repeated guesses and provide hints such as "too high" or "too low" until the number is guessed.

Concepts: while loops, conditions and loop termination.

## 32

Star and Number Patterns

Print patterns such as a right-angled triangle of stars and a number triangle using nested loops.

Concepts: nested loops, row/column relationships and output tracing.

## 4. Functions: Reusable Solutions

Problems 33–42 · Divide larger tasks into smaller, testable units.

## 33

Square and Cube Functions

Write separate functions that accept a number and return its square and cube.

Concepts: function definitions, parameters and return values.

## 34

Even/Odd Function

Write a function that accepts an integer and returns whether it is even. Use the function to classify several integers.

Concepts: Boolean return values and reuse.

## 35

Maximum of Three

Write a function that accepts three numbers and returns the largest without using Python's built-in `max()`.

Concepts: parameters, selection and return values.

## 36

Factorial Function

Implement factorial as a function. Call it for different inputs and use the returned result in another calculation.

Concepts: function reuse, local variables and return values.

## 37

Prime-Checking Function

Create a function that returns `True` if a number is prime and `False` otherwise. Use it to display all primes in a specified range.

Concepts: functions, Boolean results and loops.

## 38

Grade Calculator Functions

Write one function to calculate a percentage and another to assign a grade based on that percentage.

Concepts: decomposition, parameters and function composition.

## 39

Electrical Calculation Toolkit

Create separate functions for calculating power, resistance and energy consumed. Use appropriate formulas and document any assumptions about units and nonzero denominators.

Concepts: modular programming and technical formulas.

## 40

Vowel, Consonant and Digit Counter

Write three helper functions to count vowels, consonants and digits in a string. Ignore spaces and punctuation when classifying characters.

Concepts: strings, character classification and helper functions.

## 41

Menu-Driven Calculator

Create separate functions for addition, subtraction, multiplication and division. Display a menu and call the appropriate function based on the user's choice.

Concepts: functions, selection, loops and validation.

## 42

Student Result Processing

Write functions to calculate total marks, percentage, grade and pass/fail status. Combine them into one program that processes a student's results.

Concepts: modular design, function calls and integration.

## 5. Lists and Basic Data Processing

Problems 43–52 · Move from individual values to collections of data.

## 43

List Statistics

Input or define a list of numbers and calculate its sum, count, average, minimum and maximum without relying on built-in aggregation functions.

Concepts: lists, traversal and accumulators.

## 44

Count Even and Odd Values

Traverse a list of integers and count how many values are even and how many are odd.

Concepts: iteration, conditions and counters.

## 45

Linear Search

Search for a given value in a list. Report its index if found; otherwise, report that it is absent.

Concepts: traversal, comparisons and search flags.

## 46

Count Occurrences

Given a list and a target value, count how many times the target appears.

Concepts: loops, equality tests and counters.

## 47

Reverse a List

Create a reversed copy of a list without using slicing or the built-in `reverse()` method.

Concepts: indexing, traversal and list construction.

## 48

Find the Second-Largest Value

Find the second-largest distinct value in a list without sorting it. Report when no such value exists.

Concepts: comparisons, state tracking and edge cases.

## 49

Remove Duplicates

Construct a new list containing each value from the original list only once, preserving the original order.

Concepts: membership tests, nested iteration or sets, and order preservation.

## 50

Sort Numbers

Arrange a list in ascending order by implementing a simple sorting algorithm such as bubble sort, rather than using `sort()`.

Concepts: nested loops, swapping and algorithm tracing.

## 51

Class Marks Analysis

Store the marks of a class in a list. Calculate the class average, highest mark, lowest mark and the number of students who passed according to a specified threshold.

Concepts: list traversal, aggregation and conditional counting.

## 52

Word Frequency Counter

Input a sentence and count how many times each word occurs. For a first version, assume words are separated by spaces; later, handle punctuation and case differences.

Concepts: strings, dictionaries, iteration and text processing.

## 6. Integrated Problems: Applying Multiple Concepts

Problems 53–60 · Require students to combine several previously learned concepts.

## 53

Student Record System

Maintain a collection of student names and marks. Provide options to add a student, display all records, calculate individual percentages and identify the highest scorer.

Concepts: lists, dictionaries, functions, loops and menus.

## 54

Mini Banking System

Maintain an account balance and provide menu options for depositing money, withdrawing money, checking the balance and exiting. Validate all transactions.

Concepts: state, conditions, loops, functions and validation.

## 55

Inventory and Shopping System

Store product names, prices and available quantities. Allow the user to select products, update quantities and calculate the final bill.

Concepts: collections, loops, arithmetic and data validation.

## 56

Electricity Consumption Analyzer

Input daily electricity consumption for a month. Calculate total consumption, daily average, the highest-consumption day and an estimated bill using a specified tariff.

Concepts: lists, functions, aggregation and conditional billing.

## 57

Quiz Application

Present a sequence of multiple-choice questions, accept answers, calculate the score and display the final percentage and performance category.

Concepts: lists, dictionaries, loops, conditions and counters.

## 58

Text Analyzer

Analyze a paragraph and report the number of characters, words, sentences, vowels and digits. Extend it to find the most frequent word.

Concepts: strings, functions, dictionaries and data processing.

## 59

Expense Tracker

Allow users to enter expenses under categories such as food, transport, books and utilities. Calculate total expenditure, category-wise totals and the largest expense.

Concepts: lists, dictionaries, functions, aggregation and categorization.

## 60

Mini Examination Management System

Build a console-based program that stores student records and subject marks, calculates percentages and grades, identifies pass/fail status, ranks students by total marks and generates a class summary.

Concepts: decomposition, functions, collections, sorting, validation and integrated problem-solving.

## How I would use these problems in a 14-week semester

I would not assign all 60 as full programming assignments. Instead, use them as a problem bank from which to select short classroom exercises, laboratory tasks, homework and assessments.

| Teaching phase | Suggested problems | Classroom approach                                                                                     |
| -------------- | ------------------ | ------------------------------------------------------------------------------------------------------ |
| Weeks 1–2      | 1–10               | Trace examples, identify inputs/outputs, write algorithms and draw flowcharts before coding.           |
| Weeks 3–4      | 11–20              | Ask students to write truth tables or test cases for complicated conditions before implementation.     |
| Weeks 5–7      | 21–32              | Trace loops by hand; emphasize loop initialization, termination and updates.                           |
| Weeks 8–9      | 33–42              | Refactor earlier solutions into functions rather than introducing functions only through new problems. |
| Weeks 10–11    | 43–52              | Work with small lists and trace each iteration manually before writing the complete program.           |
| Weeks 12–14    | 53–60              | Assign integrated tasks individually or in pairs, with milestones and test cases.                      |

## Recommended teaching strategy

For students with different educational backgrounds, I would use three levels of difficulty.

Level 1

Guided practice

Problems 1–15. Provide sample input/output, a partially completed algorithm, or a flowchart where necessary. Focus on understanding rather than memorizing syntax.

Level 2

Independent practice

Problems 16–42. Ask students to identify the inputs, outputs, processing steps and edge cases before coding.

Level 3

Challenge and integration

Problems 43–60. Require students to decompose the problem, design test cases, explain their approach and improve their initial solution.

One important principle: assess the reasoning process, not just the final code. A student should be able to explain why a loop terminates, why a condition is correct, what a variable represents, and how the solution behaves for boundary cases.

For students from Electrical and Electronic Engineering diplomas, problems 10, 39 and 56 can provide familiar entry points. Students from ICS may progress quickly through basic syntax, while others may need additional practice with variables, arithmetic and tracing. All students should eventually attempt the same core learning outcomes.

My recommendation is to treat these 60 problems as a reusable bank, with the early problems forming the common foundation and the later problems providing opportunities for independent practice and deeper learning.
