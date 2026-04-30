VALID_PAYLOAD = {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "Secure@123",
    "confirm_password": "Secure@123",
}


def assert_validation_error(response, *, field=None, message=None):
    """Assert 422 response with correct structure; optionally check field or message."""
    assert response.status_code == 422
    data = response.get_json()
    assert 'validation_error' in data, f"Expected 'validation_error' key, got: {data}"
    errors = data['validation_error'].get('body_params', [])
    assert len(errors) > 0, "Expected at least one validation error in body_params"
    if field:
        fields_in_errors = [e['loc'][0] for e in errors if e.get('loc')]
        assert field in fields_in_errors, f"Expected field '{field}' in error locs, got {fields_in_errors}"
    if message:
        messages = [e.get('msg', '') for e in errors]
        assert any(message in m for m in messages), f"Expected '{message}' in error messages, got {messages}"


def test_valid_registration(client):
    response = client.post('/api/register', json=VALID_PAYLOAD)
    assert response.status_code == 201
    data = response.get_json()
    assert data['message'] == 'User registered successfully'
    assert data['user']['username'] == VALID_PAYLOAD['username']
    assert data['user']['email'] == VALID_PAYLOAD['email']


def test_response_excludes_password(client):
    response = client.post('/api/register', json=VALID_PAYLOAD)
    data = response.get_json()
    assert 'password' not in data
    assert 'password' not in data.get('user', {})


def test_no_body(client):
    response = client.post('/api/register', content_type='application/json')
    assert_validation_error(response)


def test_empty_body(client):
    response = client.post('/api/register', json={})
    assert_validation_error(response)


def test_missing_username(client):
    payload = {**VALID_PAYLOAD}
    del payload['username']
    response = client.post('/api/register', json=payload)
    assert_validation_error(response, field='username')


def test_missing_email(client):
    payload = {**VALID_PAYLOAD}
    del payload['email']
    response = client.post('/api/register', json=payload)
    assert_validation_error(response, field='email')


def test_missing_password(client):
    payload = {**VALID_PAYLOAD}
    del payload['password']
    response = client.post('/api/register', json=payload)
    assert_validation_error(response, field='password')


def test_missing_confirm_password(client):
    payload = {**VALID_PAYLOAD}
    del payload['confirm_password']
    response = client.post('/api/register', json=payload)
    assert_validation_error(response, field='confirm_password')


def test_invalid_email_format(client):
    response = client.post('/api/register', json={**VALID_PAYLOAD, 'email': 'notanemail'})
    assert_validation_error(response, field='email')


def test_username_too_short(client):
    response = client.post('/api/register', json={**VALID_PAYLOAD, 'username': 'ab'})
    assert_validation_error(response, field='username')


def test_username_too_long(client):
    response = client.post('/api/register', json={**VALID_PAYLOAD, 'username': 'a' * 51})
    assert_validation_error(response, field='username')


def test_username_invalid_chars(client):
    response = client.post('/api/register', json={**VALID_PAYLOAD, 'username': 'john doe!'})
    assert_validation_error(response, field='username')


def test_password_too_short(client):
    response = client.post('/api/register', json={**VALID_PAYLOAD, 'password': 'Ab1@', 'confirm_password': 'Ab1@'})
    assert_validation_error(response, field='password', message='at least 8 characters')


def test_password_no_uppercase(client):
    response = client.post('/api/register', json={**VALID_PAYLOAD, 'password': 'secure@123', 'confirm_password': 'secure@123'})
    assert_validation_error(response, field='password', message='uppercase')


def test_password_no_lowercase(client):
    response = client.post('/api/register', json={**VALID_PAYLOAD, 'password': 'SECURE@123', 'confirm_password': 'SECURE@123'})
    assert_validation_error(response, field='password', message='lowercase')


def test_password_no_digit(client):
    response = client.post('/api/register', json={**VALID_PAYLOAD, 'password': 'Secure@abc', 'confirm_password': 'Secure@abc'})
    assert_validation_error(response, field='password', message='digit')


def test_password_no_special_char(client):
    response = client.post('/api/register', json={**VALID_PAYLOAD, 'password': 'Secure1234', 'confirm_password': 'Secure1234'})
    assert_validation_error(response, field='password', message='special character')


def test_passwords_do_not_match(client):
    response = client.post('/api/register', json={**VALID_PAYLOAD, 'confirm_password': 'Different@123'})
    assert_validation_error(response, message='Passwords do not match')


def test_duplicate_email_returns_409(client):
    client.post('/api/register', json=VALID_PAYLOAD)
    response = client.post('/api/register', json=VALID_PAYLOAD)
    assert response.status_code == 409
    assert response.get_json()['error'] == 'Email already registered'


def test_user_not_stored_with_password(client):
    from app.users import user_store
    client.post('/api/register', json=VALID_PAYLOAD)
    stored = user_store._data.get(VALID_PAYLOAD['email'])
    assert stored is not None
    assert 'password' not in stored
    assert 'confirm_password' not in stored