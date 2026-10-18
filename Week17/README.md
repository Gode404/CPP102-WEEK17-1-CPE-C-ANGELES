# Simulated Device Monitoring and Alert System

Student Name: Richard O. Angeles
Student Number: 2601301
Section: 1-CPE-C

## Project Description

This program monitors simulated device temperature readings. It classifies each reading as NORMAL, WARNING, or CRITICAL and prints a summary with the overall status. It rejects invalid readings and invalid menu choices without crashing.

## Features

- View all stored temperature readings
- Add a new reading (whole numbers from 0 to 100 only)
- Classify every reading
- Generate a numerical summary and overall status
- Reject invalid menu choices and invalid readings

## Requirements

- Python 3 (no external packages)

## How to Run

1. Open a terminal inside the Week17 folder.
2. Type: python device_monitor.py
   (On macOS or Linux, type: python3 device_monitor.py)

## Sample Output

## MONITORING SUMMARY

Number of readings : 5
Total of readings : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL : 2 (40.00%)
WARNING : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED

## Test Cases

I performed 10 tests. 10 passed and 0 failed.
Full details are in test_cases.md.

## Known Limitations

- Readings are lost when the program closes.
- Readings cannot be edited or deleted.

## Reflection

The hardest part of this project was making all the functions work together while keeping each one to a single job. I also had to be careful with the boundary values 30 and 35, because both must be classified as WARNING. I tested them by adding 30 and running the classification, and the results matched the rules. This project showed me how lists, loops, selection, and functions with parameters and return values combine in one program, and why input must be checked in order: empty, then format, then range. Next, I would improve it by saving the readings so they are not lost when the program closes.
