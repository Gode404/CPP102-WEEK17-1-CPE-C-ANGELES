# Test Cases - Simulated Device Monitoring and Alert System

Tested by: Richard O. Angeles Date: 10/18/2026

| Test Case | Input or Action         | Expected Result                                                 | Actual Result                                                                     | Pass/Fail |
| --------- | ----------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------- |
| TC01      | Choose 1                | Five readings: 28, 31, 35, 37, 29                               | Showed Reading 1 to 5: 28, 31, 35, 37, 29 °C                                      | Pass      |
| TC02      | Choose 2, enter 33      | Reading added successfully                                      | "Reading added successfully."; Reading 6: 33 °C appeared in the list              | Pass      |
| TC03      | Choose 2, enter abc     | Rejected; list unchanged                                        | "Invalid input. Enter a whole number only."; list still had 5 readings            | Pass      |
| TC04      | Choose 2, enter -5      | Rejected; list unchanged                                        | "Invalid reading. Enter a value from 0 to 100."; list still had 5 readings        | Pass      |
| TC05      | Choose 2, enter 120     | Rejected; list unchanged                                        | "Invalid reading. Enter a value from 0 to 100."; list still had 5 readings        | Pass      |
| TC06      | Add 30, then choose 3   | 30 °C -> WARNING                                                | 30 °C -> WARNING                                                                  | Pass      |
| TC07      | Choose 3                | 35 °C -> WARNING                                                | 35 °C -> WARNING                                                                  | Pass      |
| TC08      | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED | Total 160, Avg 32.00 °C, Min 28 °C, Max 37 °C, Overall Status: ATTENTION REQUIRED | Pass      |
| TC09      | Enter 9                 | Error message; menu shown again                                 | "Invalid choice. Please enter a number from 1 to 5."; menu displayed again        | Pass      |
| TC10      | Choose 5                | Exit message; program ends                                      | "Thank you for using the Device Monitoring System."; program ended                | Pass      |

## Bugs Found and Fixed

-I did not find a failing test. The hardest to pass were TC06 and TC07, because the boundary values 30 and 35 must both be WARNING. When I ran Classify Readings, the program printed "30 °C -> WARNING" and "35 °C -> WARNING", which matched the rule.
