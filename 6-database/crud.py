from index import db, Puppy

# Create
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

# Read
all_puppies = Puppy.query.all() # list of all puppies objects in the table
print(all_puppies)

# select by id
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# Filter
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())
# ['Frankie is 3 years old]

# update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# delete
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)
