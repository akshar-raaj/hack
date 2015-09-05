import redis

r = redis.StrictRedis()

def get_current_person_count():
    person_count = r.get("person_count")
    if person_count is None:
        # No person yet
        return 0
    return int(person_count)

def set_person_count(person_count):
    r.set("person_count", person_count)

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save(self):
        person_count = get_current_person_count()
        person_id = person_count + 1
        rep = "person:" + str(person_id)
        r.hset(rep, "name", self.name)
        r.hset(rep, "age", self.age)
        set_person_count(person_id)