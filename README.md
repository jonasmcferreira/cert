# SAP-C02 Practice Exam

## Quick Start

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000` in your browser.

## Features

- **Mini Test**: 30 random questions from unanswered pool
- **Full Exam**: 75 random questions from unanswered pool  
- **Study Mode**: Browse all questions at your own pace
- **Progress Tracking**: Uses localStorage to track answered questions
- **Interactive UI**: Radio buttons for single answers, checkboxes for multi-select
- **Keyboard Shortcuts**: Arrow keys for navigation, spacebar to reveal answers, 1-6 keys to select choices
- **Explanations**: Detailed explanations for correct and incorrect answers

## Static Deployment

```bash
cp templates/home.html index.html
cp templates/index.html exam.html
python -m http.server 8000
```
