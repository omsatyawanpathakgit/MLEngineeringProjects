# CI/CD Pipeline - Book Recommender System

This folder contains GitHub Actions workflows for testing the Book Recommender System project.

## Primary Test Workflow

### **test.yml** - Book Recommender Test Suite ⭐
- **Triggers:** Push to `main` or `develop` branches, Pull Requests
- **Python Version:** 3.9
- **Test Cases:**
  1. ✓ **No recommendations for empty book name** - Validates that empty input is handled gracefully
  2. ✓ **Display recommendations** - Ensures recommendations are properly displayed
  3. ✓ **No duplicate recommendations** - Verifies duplicate filtering works correctly
  4. ✓ **Input book not in recommendations** - Confirms the searched book is not recommended

**Run Command:**
```bash
cd book_recommender_flask
pytest tests/test_recommendations.py -v
```



## Test File Structure

```
book_recommender_flask/
├── tests/
│   ├── __init__.py
│   └── test_recommendations.py    ← Main test file with 4 test cases
├── app.py
├── requirements.txt
└── ...
```

## How to Run Tests Locally

1. **Install dependencies:**
   ```bash
   cd book_recommender_flask
   pip install -r requirements.txt pytest
   ```

2. **Run all tests:**
   ```bash
   pytest tests/test_recommendations.py -v
   ```

3. **Run specific test:**
   ```bash
   pytest tests/test_recommendations.py::TestRecommendations::test_no_recommendations_for_empty_book_name -v
   ```

## Test Details

### Test Case 1: Empty Book Name
```python
def test_no_recommendations_for_empty_book_name(self, client):
```
- Input: Empty string as book name
- Expected: No recommendations or error message
- Purpose: Ensure input validation

### Test Case 2: Display Recommendations
```python
def test_display_recommendations(self, client):
```
- Input: Valid book name (e.g., 'Harry Potter')
- Expected: Recommendations displayed in response
- Purpose: Verify core functionality

### Test Case 3: No Duplicate Recommendations
```python
def test_no_duplicate_recommendations(self, client):
```
- Input: Valid book name
- Expected: Each recommended book appears only once
- Purpose: Ensure quality of recommendations

### Test Case 4: Input Book Not in Recommendations
```python
def test_dont_recommend_input_book_itself(self, client):
```
- Input: Valid book name
- Expected: Input book does not appear in recommendations
- Purpose: Avoid recommending the same book

## CI/CD Status

GitHub Actions will run automatically when you:
- Push to `main` or `develop` branch
- Create a Pull Request

Check the **Actions** tab in your GitHub repository to view:
- ✅ Test results
- ❌ Failed tests
- 📊 Test coverage

## Requirements

Ensure `book_recommender_flask/requirements.txt` includes:
- Flask
- pandas
- scikit-learn (or similar ML library)
- pytest (for testing)
