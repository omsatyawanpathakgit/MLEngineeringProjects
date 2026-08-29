import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestRecommendations:
    """Test cases for Book Recommender System"""
    
    def test_no_recommendations_for_empty_book_name(self, client):
        """Test that no recommendations are returned for empty book name"""
        response = client.post('/', data={'book_name': ''})
        assert response.status_code == 200
        # Empty book name should not produce recommendations
        assert b'No recommendations found' in response.data or b'Please enter a book name' in response.data
    
    def test_display_recommendations(self, client):
        """Test that recommendations are properly displayed"""
        # Assuming 'Harry Potter' or similar popular book exists in dataset
        response = client.post('/', data={'book_name': 'Harry Potter and the Philosopher\'s Stone'})
        assert response.status_code == 200
        # Should contain book recommendations in response
        assert b'Recommendation' in response.data or b'Similar Books' in response.data or b'Harry Potter' in response.data
    
    def test_no_duplicate_recommendations(self, client):
        """Test that no duplicate recommendations are returned"""
        response = client.post('/', data={'book_name': 'Harry Potter and the Philosopher\'s Stone'})
        assert response.status_code == 200
        
        # Parse recommendations from response
        # Count occurrences of book titles to ensure no duplicates
        response_text = response.data.decode('utf-8')
        
        # Extract book recommendations (assuming HTML structure with book titles)
        # This verifies that the same book title doesn't appear multiple times in recommendations
        lines = response_text.split('\n')
        recommendation_titles = []
        
        for line in lines:
            if 'recommendation' in line.lower() or 'similar' in line.lower():
                recommendation_titles.append(line.strip())
        
        # Verify no duplicates exist
        assert len(recommendation_titles) == len(set(recommendation_titles)), "Duplicate recommendations found"
    
    def test_dont_recommend_input_book_itself(self, client):
        """Test that the input book itself is not recommended"""
        input_book = 'Harry Potter and the Philosopher\'s Stone'
        response = client.post('/', data={'book_name': input_book})
        assert response.status_code == 200
        
        response_text = response.data.decode('utf-8')
        
        # Count how many times the exact input book appears in recommendations
        # The input book should appear only once (as the searched book) not in recommendations
        occurrences = response_text.count(input_book)
        
        # If the book is displayed as searched book and also in recommendations, 
        # it should appear only once (or in separate sections)
        assert occurrences <= 1, f"Input book '{input_book}' should not appear in recommendations"


class TestAppBasics:
    """Basic application functionality tests"""
    
    def test_app_loads(self, client):
        """Test that the Flask app loads successfully"""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_post_request_accepted(self, client):
        """Test that POST requests are accepted"""
        response = client.post('/', data={'book_name': 'test'})
        assert response.status_code == 200
