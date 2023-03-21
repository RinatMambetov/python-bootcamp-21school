import random
import unittest


def turrets_generator():
    personality_traits = ['neuroticism', 'openness', 'conscientiousness', 'extraversion', 'agreeableness']
    actions = ['shoot', 'search', 'talk']
    remaining_percentage = 100

    while True:
        if remaining_percentage == 0:
            break

        random_numbers = [random.randint(0, remaining_percentage) for _ in range(len(personality_traits))]
        sum_numbers = sum(random_numbers)
        # Scale the numbers so that they add up to total
        trait_percentages = [int(n * remaining_percentage / sum_numbers) for n in random_numbers]
        trait_percentages[-1] += remaining_percentage - sum(trait_percentages)
        personality = dict(zip(personality_traits, trait_percentages))

        turret = type('Turret', (), personality)

        for action in actions:
            def action_method(act=action):
                print(act.capitalize() + 'ing')

            setattr(turret, action, action_method)

        yield turret


class TestTurretsGenerator(unittest.TestCase):

    def setUp(self):
        self.turrets = turrets_generator()

    def test_personality(self):
        turret = next(self.turrets)
        personality = [turret.neuroticism, turret.openness, turret.conscientiousness, turret.extraversion,
                       turret.agreeableness]
        self.assertEqual(sum(personality), 100)

    def test_actions(self):
        turret = next(self.turrets)
        actions = ['shoot', 'search', 'talk']
        for action in actions:
            self.assertTrue(hasattr(turret, action))
            method = getattr(turret, action)
            self.assertTrue(callable(method))


if __name__ == '__main__':
    turrets = turrets_generator()
    for i in range(10):
        t = next(turrets)
        print(f'Turret {i + 1}:\n'
              f'neuroticism {t.neuroticism}, '
              f'openness {t.openness}, '
              f'conscientiousness {t.conscientiousness}, '
              f'extraversion {t.extraversion}, '
              f'agreeableness {t.agreeableness}')
        t.shoot()
        t.search()
        t.talk()

    unittest.main()
