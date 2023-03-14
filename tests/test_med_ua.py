from ref_clinic.models import Doctor, Record    

"""initial test"""
def test_home(client):
    response = client.get('/')
    assert b"<title>EPAM Med</title>" in response.data
    

def test_createdoctor(client, app):
    response = client.post("/create_doctor", data={"email": "test@test.com",
                                                   "name": "testname",
                                                   "specialization": "tester",
                                                   "years_xp": 11})
    with app.app_context():
        assert Doctor.query.count() == 1
        assert Doctor.query.first().email == "test@test.com"
        assert Doctor.query.first().years_xp == 11


def test_update_doc(client, app):
    client.post("/create_doctor", data={"email": "test@test.com",
                                                   "name": "testname",
                                                   "specialization": "tester",
                                                   "years_xp": 11})
    client.post("/update/1", data={"email": "update@test.com",
                                                   "name": "upname",
                                                   "specialization": "tester",
                                                   "years_xp": 7})
    
    with app.app_context():
        assert Doctor.query.count() == 1
        assert Doctor.query.first().email == "update@test.com"
        assert Doctor.query.first().name == "upname"
        assert Doctor.query.first().years_xp == 7
        

def test_doctor_update_2(client, app):
    """ testing the ability to update a single doctor""" 
    client.post("/create_doctor", data={"email": "test@test.com",
                                                   "name": "testname",
                                                   "specialization": "tester",
                                                   "years_xp": 11})
    client.post("/update/1", data={"email": "update@test.com",
                                                   "name": "upname",
                                                   "specialization": "tester",
                                                   "years_xp": 7})
    
    with app.app_context():
        assert Doctor.query.count() == 1
        assert Doctor.query.first().email == "update@test.com"
        assert Doctor.query.first().name == "upname"
        assert Doctor.query.first().years_xp == 7


def test_doctor_delete(client, app):
    """ testing the ability to delete a single doctor""" 
    client.post("/create_doctor", data={"email": "test@test.com",
                                                   "name": "testname",
                                                   "specialization": "tester",
                                                   "years_xp": 11})
    with app.app_context():
        assert Doctor.query.count() == 1
        
    client.post("/delete_doctor/1")
    with app.app_context():
        assert Doctor.query.count() == 0
        assert Doctor.query.first() is None


# def test_search(client, app):
#     """ testing the ability to create record"""
#     client.post("/search", form={"searched": 'te'})
#     with app.app_context():
#         assert Record.query.count() == 1
#         assert Record.query.first().data == "some info"
#         assert Record.query.first().doctor_id == 1
