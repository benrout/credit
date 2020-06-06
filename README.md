# credit
A program that determines whether a provided credit card number is valid according to [Luhn’s algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm).

It then checks if what type of card it is based on the following criteria:
* American Express - 15-digit number starting with 34 or 37
* Mastercard - 16-digit number starting with 51, 52, 53, 54, 55
* Visa - 13-digit or 16-digit number starting with 4

Example usage:
```
$ python credit.py
Number: 378282246310005
AMEX
```