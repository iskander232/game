import random
from strategy import *
from unit import *
from consts import *


class examenator(Unit):
    def __str__(self):
        return '{}, name = {}, subject = {}, knowlege = {}, easiness = {}, alcohol_liking = {}, friendliness = {}, sex = {}'.format(
            self.type, self.name, self.subject,
            self.knowlege, self.easiness, self.alcohol_liking, self.friendliness, self.sex)


class lecturer(examenator):
    type = 'lecturer'


class seminarist(examenator):
    type = 'seminarist'


class lecturers_factory:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def create_examenator(self):
        lecturer_1 = lecturer()
        lecturer_1.knowlege = int(random.normalvariate(lecturer_knowlege / self.difficulty, 2) % max_stat)
        lecturer_1.easiness = int(random.normalvariate(lecturer_easiness / self.difficulty, 2) % max_stat)
        lecturer_1.friendliness = int(random.normalvariate(lecturer_friendliness / self.difficulty, 2) % max_stat)
        lecturer_1.friendliness = int(random.normalvariate(lecturer_friendliness / self.difficulty, 2) % max_stat)
        lecturer_1.alcohol_liking = int(random.normalvariate(lecturer_alcohol_liking / self.difficulty, 2) % max_stat)
        y = random.randint(0, lecturers_name.__len__() - 1)
        lecturer_1.name = lecturers_name[y].name
        lecturer_1.subject = lecturers_name[y].subject
        lecturer_1.sex = lecturers_name[y].sex
        return lecturer_1


class seminarists_factory:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def create_examenator(self, subject=subjects[random.randint(0, subjects.__len__() - 1)]):
        seminarist_1 = seminarist()
        seminarist_1.knowlege = int(random.normalvariate(seminarist_knowlege / self.difficulty, 2) % max_stat)
        seminarist_1.easiness = int(random.normalvariate(seminarist_easiness / self.difficulty, 2) % max_stat)
        seminarist_1.friendliness = int(random.normalvariate(seminarist_friendliness / self.difficulty, 2) % max_stat)
        seminarist_1.alcohol_liking = int(
            random.normalvariate(seminarist_alcohol_liking / self.difficulty, 2) % max_stat)
        a = seminarists[subject][random.randint(0, seminarists[subject].__len__() - 1)]
        seminarist_1.name = a.name
        seminarist_1.subject = a.subject
        seminarist_1.sex = a.sex
        return seminarist_1


def give_examenator_factory(examenator, *args):
    if examenator == 'lecturer':
        return lecturers_factory(*args)
    elif examenator == 'seminarist':
        return seminarists_factory(*args)
