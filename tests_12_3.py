import unittest
from functools import wraps


def skip_is_frozen(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return func(self, *args, **kwargs)

    return wrapper


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_is_frozen
    def test_walk(self):
        runner = Runner('')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_is_frozen
    def test_run(self):
        runner = Runner('')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_is_frozen
    def test_challenge(self):
        runner1 = Runner("")
        runner2 = Runner("")
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)

    def setUp(self):
        self.all_results = {}
        self.first_runner = Runner("Усэйн", 10)
        self.second_runner = Runner("Андрей", 9)
        self.third_runner = Runner("Ник", 3)

    @skip_is_frozen
    def test_tournament1(self):
        tournament = Tournament(90, self.first_runner, self.third_runner)
        self.all_results = tournament.start()
        self.assertEqual(self.all_results[max(self.all_results)], "Ник")
        TournamentTest.all_results["first"] = self.all_results

    @skip_is_frozen
    def test_tournament2(self):
        tournament = Tournament(90, self.second_runner, self.third_runner)
        self.all_results = tournament.start()
        self.assertEqual(self.all_results[max(self.all_results)], "Ник")
        TournamentTest.all_results["second"] = self.all_results

    @skip_is_frozen
    def test_tournament3(self):
        tournament = Tournament(90, self.first_runner, self.second_runner, self.third_runner)
        self.all_results = tournament.start()
        self.assertEqual(self.all_results[max(self.all_results)], "Ник")
        TournamentTest.all_results["third"] = self.all_results


if __name__ == '__main__':
    unittest.main()
