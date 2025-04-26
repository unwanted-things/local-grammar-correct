# Local Grammar Correct 🎯

A fun CLI tool for local grammar correction and text analysis. Built with AI assistance, so double-check before using! 😉


## Features

- ✨ Grammar checking
- 📝 Spelling correction
- 📊 Text analysis
- 🔒 Runs completely locally

## Installation

```bash
# Clone the repository
git clone https://github.com/unwanted-things/local-grammar-correct.git
cd local-grammar-correct

# Install the package
pip install -e .
```

## Usage

```bash
# Correct grammar and spelling
local-grammar-correct correct "Your text here"

# Analyze text
local-grammar-correct analyze "Your text here"
```

## Example

```bash
$ local-grammar-correct correct "Their going to the store yesterday, but they're car broke down. Its a shame."

✨ Grammar Correction ✨

Original text:
Their going to the store yesterday, but they're car broke down. Its a shame.

Corrected text:
They're going to the store yesterday, but their car broke down. It's a shame.

📝 Spelling Corrections
✗ Their → They're
✗ they're → their
✗ Its → It's

📝 Grammar Issues
Articles:
⚠️  Use 'an' before 'hour'
⚠️  Use 'a' before 'university'

Verb Tense:
⚠️  Verb tense inconsistency detected
```

## Warning ⚠️

This project was coded with AI assistance. While it's fun to use, please double-check its suggestions before relying on them for important work. It's all about the vibe! 🎉

## License

MIT License - Feel free to use and modify! 