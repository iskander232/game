from enum import Enum


class person:
    def __init__(self, p_name, p_subject, p_sex='man', p_picture=None):
        self.name = p_name
        self.subject = p_subject
        self.picture = p_picture
        self.sex = p_sex

    def __eq__(self, other):
        if type(other) == person and self.subject == other.subject and self.name == other.name:
            return True
        else:
            return False


class Subjects(Enum):
    OKTCH = 'OKTCH'
    matan = 'matan'
    matlog = 'matlog'


class Manager(Enum):
    bot = 'bot'
    player = 'player'


unitSpeed = 10
dist = 6
student_stat = 10
max_stat = 10
student_health = range(100, 200)
seminarist_health = range(200, 300)
lecturer_health = range(300, 400)
lecturer_knowlege_min = 9
lecturer_knwlege_max = 10
lecturer_easiness_min = 7
lecturer_easiness_max = 10
seminarist_knowlege_min = 7
seminarist_knwlege_max = 10
seminarist_easiness_min = 5
seminarist_easiness_max = 10
lecturer_friendliness_min = 0
lecturer_friendliness_max = 5
seminarist_friendliness_min = 0
seminarist_friendliness_max = 7
lecturer_alcohol_liking_min = 0
lecturer_alcohol_liking_max = 8
seminarist_alcohol_liking_min = 3
seminarist_alcohol_liking_max = 10
seminarists = dict()
subjects = ['matan', 'OKTCH', 'matlog']
seminarists['matan'] = (
    person('Ivanova', 'matan', 'woman', 'pictures.ivanova'), person('Kuzmenko', 'matan', 'pictures.kuzmenko'),
    person('Starodubcev', 'matan'))
seminarists['OKTCH'] = (person('Grigoriev', 'OKTCH', 'pictures.grigoriev'), person('Glibenchuk', 'OKTCH'),
                        person('Iliinskiy', 'OKTCH', 'pictures.ilinskiy'))
seminarists['matlog'] = (person('Irhin', 'matlog'), person('Milovanov', 'matlog'), person('Ivachenko', 'matlog'))

lecturers_name = [person('Musatov', 'mathlog', 'pictures.musatov'), person('Raygor', 'OKTCH', 'pictures.raygor'),
                  person('Redkozubov', 'matan', 'pictures.redkozubov')]
