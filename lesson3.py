class Junior:
    def __init__(self, name, salary, laptop, language):
        self.name = name
        self.salary = salary
        self.laptop = laptop
        self.language = language

    def say_which_language(self):
        return f"I'm using {self.language}"

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Salary: {self.salary}\n' \
               f'Laptop: {self.laptop}\n' \
               f'Language: {self.language}\n'


junior = Junior(name='Adahan', salary='150', laptop='Asus VivoBook', language='Python')
print(junior)
print(junior.say_which_language())
print('-' * 50)


class Middle(Junior):
    def __init__(self, name, salary, laptop, language, experience, car, frilance):
        super(Middle, self).__init__(name, salary, laptop, language)
        self.experience = experience
        self.car = car
        self.frilance = frilance

    def say_which_language(self):
        return f"I'm using {self.language}"

    def __str__(self):
        return super(Middle, self).__str__() + f'experience: {self.experience}\n' \
                                               f'Car: {self.car}\n' \
                                               f'Frilance: {self.frilance}\n'


middle = Middle(name='Adilet', salary='2500', laptop='Macbook Air 2021',
                language='Python, Java',
                experience='3 year', car=True, frilance='Japan')
print(middle)
print(middle.say_which_language())
print('-' * 50)


class Senior(Middle):
    def __init__(self, name, salary, laptop, language, experience, car, frilance, status, leading_skills):
        super(Senior, self).__init__(name, salary, laptop, language, experience, car, frilance)
        self.status = status
        self.leading_skills = leading_skills

    def say_which_language(self):
        return f"I'm using {self.language}"

    def __str__(self):
        return super(Senior, self).__str__() + f'Status: {self.status}\n' \
                                               f'Leading_skills: {self.leading_skills}\n'


senior = Senior(name='Malik', salary='5000', laptop='Macbook pro 2021', language='Python, JS',
                experience='5 year', car='Lexus', frilance='German', status='Senior', leading_skills=True)
print(senior)
print(senior.say_which_language())

