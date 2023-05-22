from src.schemas import people

# для поиска пользователя в списке people
def find_person(id):
   for person in people: 
        if person.id == id:
           return person
   return None
