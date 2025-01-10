# import pytest
# from rest_framework.test import APIClient

# client = APIClient()

# @pytest.mark.django_db
# #
# def test_register_user():
#     payload=dict(
        
#             username= "Sanjay",
#             password= "Sanjay@123",
#             password2= "Sanjay@123",
#             email= "sanjay@gmail.com",
#             first_name= "Sanjay",
#             last_name= "R"
        
#     )
#     response = client.post('/api/user/register',payload)
#     data = response.data
#     assert data['status'] ==201
#     assert data['message'] =='User added Successfully'
