# python-assignment

---

## 1. GCD Calculator (Word to Word)

This script calculates the **Greatest Common Divisor (GCD)** of two numbers provided in **word format** (e.g., "one", "two", "three").

## Features
- Converts numbers between **words and digits**.
- Uses **recursive Euclidean Algorithm** to compute the GCD.
- Uses the **Singleton design pattern** for number conversion.
- Tracks execution time with a **decorator**.

## Example
- Input: Enter first number in words: six 
- Input: Enter second number in words: eight 
- Output: `GCD in words: two`


## 2. Generate Valid Parentheses

This script generates **all valid combinations** of `n` pairs of parentheses using a **recursive backtracking algorithm**.

## Features
- Generates all valid combinations for a given number of pairs (`n`).
- Validates input to ensure `n` is between **1 and 8**.
- Uses a **decorator** to measure and display execution time.

## Example
- Input: Enter Number in range of 1 to 8: 3 
- Output: `['((()))', '(()())', '(())()', '()(())', '()()()']`


## 3. Anagram Words Grouping

This script groups a list of words into **anagram groups**, where each group contains words that are anagrams of each other (contain the same letters in different order).

## Features
- Accepts a **space-separated list** of words.
- Uses **character frequency counting** to identify and group anagrams.
- Groups words into lists using a **dictionary-based approach**.
- Tracks execution time with a **decorator**.

## Example

- Input: Enter space separated words: eat tea tan ate nat bat 
- Output: `[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]`