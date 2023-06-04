![Status](https://github.com/kguryanov/FizzBuzz/actions/workflows/flow.yml/badge.svg?branch=break_tests)

{r, echo=FALSE, eval=TRUE, results="asis"}
shield <- paste0("[![Build Status](",
                 system("git rev-parse --abbrev-ref HEAD", intern = TRUE),
                 ")](https://travis-ci.org/RevolutionAnalytics/miniCRAN)")
cat(shield)


## Question:
Write a Python program that iterates the integers from 1 to 50. For multiples of
three print "Fizz" instead of the number and for multiples of five print "Buzz". For
numbers that are multiples of three and five, print "FizzBuzz"

## Instructions:
Please provide the code, any workings and the expected output

## Usage 
<code>$> python main.py</code>

![image](https://github.com/kguryanov/FizzBuzz/assets/3843209/39582b31-0f87-48c1-8bc1-1ea8ff4affb6)


## Run tests (requires pytest to be installed)
### Install pytest:
<code>$> python -m pip install -r requirements.txt</code>
### Run tests
<code>$> python -m pytest</code>

## Tests with coverage (external packages)
### Install coverage ():
<code>$>python -m pip install -r requirements.txt</code>
### Run tests with coverage:
<code>$>python -m coverage run -m pytest</code>

<code>$>python -m coverage html</code>

Html report shall be available in `htmlcov` folder. 

