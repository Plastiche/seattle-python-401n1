from faker import Faker
import shutil

fake = Faker('en_US')

# print(fake)

# print(dir(fake))

# print(fake.words())

# print(fake.paragraph())
#
# print(fake.email())
#
# print(fake.phone_number())

content = ''

for _ in range(100):
    content += fake.paragraph()
    content += fake.email()
    content += fake.paragraph()
    content += fake.phone_number()
    content += fake.paragraph()

print(content)

with open('notes.txt', 'w+') as f:
    f.write(content)

shutil.copy('notes.txt', '../../assets')
