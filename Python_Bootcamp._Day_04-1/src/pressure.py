import random
import time
import unittest


def emit_gel(step):
    value = 50
    while True:
        value += round(random.uniform(0, step))
        if value > 100:
            raise ValueError(f"Measured pressure out of range: {value}")
        signal = yield value
        if signal == 'rev':
            step = -step
        time.sleep(0.001)


def valve(step):
    gen = emit_gel(step)
    while True:
        try:
            value = next(gen)
            if value < 10 or value > 90:
                gen.close()
                break
            if value < 20 or value > 80:
                gen.send('rev')
            yield value
        except ValueError as e:
            print(f"Error: {e}")


class TestEmitGel(unittest.TestCase):

    def test_pressure_values(self):
        gen = emit_gel(5)
        for i in range(10):
            pressure = next(gen)
            self.assertGreaterEqual(pressure, 50)
            self.assertLessEqual(pressure, 100)

    def test_value_error(self):
        gen = emit_gel(10)
        with self.assertRaises(ValueError):
            for i in range(200):
                next(gen)


if __name__ == '__main__':
    for p in valve(10):
        print(p)

    unittest.main()
