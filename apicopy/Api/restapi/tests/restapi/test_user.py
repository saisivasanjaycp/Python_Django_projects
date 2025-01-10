import pytest
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db

def test_register_user():
    payload=dict(
        
            username= "Devanathan",
            password= "Sai",
            password2= "Sai123",
            email= "sai@gmail.com",
            first_name= "Sajay",
            last_name= "R"
        
    )
    response = client.post('/api/user/register',payload)
    data = response.data
    assert data['status'] ==201
    assert data['message'] =='User added successfully'
