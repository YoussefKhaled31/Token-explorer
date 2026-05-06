# Token Explorer CLI

A simple Python command-line tool that shows how text is split into tokens using OpenAI's `tiktoken` library.

## What it does

You type any text into the terminal, and the program generates a clear token report showing the token count, prompt size, token IDs, token pieces, and the decoded text.

This helps make tokenization easier to understand, especially for people learning how Large Language Models process text.

## Features

- Counts the number of tokens in your text
- Labels the prompt as short, medium, or long
- Shows the token IDs
- Shows each token piece separately
- Decodes the tokens back into text
- Runs directly from the command line

## Why I made it

I made this project to better understand how Large Language Models break text into tokens before processing it. It was also a way for me to practice Python functions, loops, conditionals, user input, and working with external libraries.

## How to run

Install `tiktoken` by running `pip install tiktoken`.

Then run the project with `python token_explorer.py`.

## Example

If you enter:

`Explain black holes simply.`

The program will show a token report with the token count, token IDs, and the individual token pieces.
