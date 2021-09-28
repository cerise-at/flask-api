users = [
{"id": 1, "username": "jon", "age": 4}
]

def all():
    return [user for user in users]

def create(data):
    user = data.get_json()
    user["id"] = len(users) + 1
    users.append(user)
    return user, 201

def find_by_id(id):
    user = [user for user in users if user['id'] == id]
    # user = [users.filter(lambda users['id'] == id)]
    print(user)
