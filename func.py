class Dog:
    name = None # атрибуты
    age = None
    isHappy = True

dog1 = Dog() # это экземпляр класса
dog1.name = 'Alfa'
dog1.age = 2
dog1.isHappy = True
print('name: ', dog1.name, 'age:', dog1.age, dog1.isHappy)

dog2 = Dog() # это экземпляр класса
dog2.name = 'Bob'
dog2.age = 5
dog2.isHappy = False
print('name: ', dog2.name, 'age:', dog2.age, dog2.isHappy)