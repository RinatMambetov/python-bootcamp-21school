import unittest
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from unittest.mock import MagicMock
from urllib.parse import urlencode

DEFAULT_SPECIES = 'Unknown'

list_of_species = {
    'Cyberman': 'John Lumic',
    'Dalek': 'Davros',
    'Judoon': 'Shadow Proclamation Convention 15 Enforcer',
    'Human': 'Leonardo da Vinci',
    'Ood': 'Klineman Halpen',
    'Silence': 'Tasha Lem',
    'Slitheen': 'Coca-Cola salesman',
    'Sontaran': 'General Staal',
    'Time Lord': 'Rassilon',
    'Weeping Angel': 'The Division Representative',
    'Zygon': 'Broton',
    DEFAULT_SPECIES: DEFAULT_SPECIES
}


def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    species = d.get('species', [DEFAULT_SPECIES])[0]
    name = list_of_species.get(species, DEFAULT_SPECIES)

    response_body = f'{{"credentials": "{name}"}}\n'.encode('UTF-8')
    status = '200 OK' if name != DEFAULT_SPECIES else '404 Not found'
    response_headers = [
        ('Content-Type', 'text/plain; charset=utf-8'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    return [response_body]


def main():
    host, port = 'localhost', 8888
    server = make_server(host, port, application)
    print(f'Serving HTTP on port {port}...')
    server.serve_forever()


class TestApplication(unittest.TestCase):
    def setUp(self):
        self.environ = {
            'QUERY_STRING': '',
        }
        self.start_response = MagicMock()

    def test_returns_default_when_no_species_provided(self):
        result = application(self.environ, self.start_response)
        self.start_response.assert_called_with('404 Not found', [
            ('Content-Type', 'text/plain; charset=utf-8'),
            ('Content-Length', '27')
        ])
        self.assertEqual(result, [b'{"credentials": "Unknown"}\n'])

    def test_returns_cyberman_credentials(self):
        self.environ['QUERY_STRING'] = urlencode({'species': 'Cyberman'})
        result = application(self.environ, self.start_response)
        self.start_response.assert_called_with('200 OK', [
            ('Content-Type', 'text/plain; charset=utf-8'),
            ('Content-Length', '30')
        ])
        self.assertEqual(result, [b'{"credentials": "John Lumic"}\n'])

    def test_returns_weeping_angel_credentials(self):
        self.environ['QUERY_STRING'] = urlencode({'species': 'Weeping Angel'})
        result = application(self.environ, self.start_response)
        self.start_response.assert_called_with('200 OK', [
            ('Content-Type', 'text/plain; charset=utf-8'),
            ('Content-Length', '47')
        ])
        self.assertEqual(result, [b'{"credentials": "The Division Representative"}\n'])

    def test_returns_default_when_species_not_found(self):
        self.environ['QUERY_STRING'] = urlencode({'species': 'Invalid Species'})
        result = application(self.environ, self.start_response)
        self.start_response.assert_called_with('404 Not found', [
            ('Content-Type', 'text/plain; charset=utf-8'),
            ('Content-Length', '27')
        ])
        self.assertEqual(result, [b'{"credentials": "Unknown"}\n'])

    def test_returns_default_when_empty_species_provided(self):
        self.environ['QUERY_STRING'] = urlencode({'species': ''})
        result = application(self.environ, self.start_response)
        self.start_response.assert_called_with('404 Not found', [
            ('Content-Type', 'text/plain; charset=utf-8'),
            ('Content-Length', '27')
        ])
        self.assertEqual(result, [b'{"credentials": "Unknown"}\n'])


if __name__ == '__main__':
    # unittest.main()
    main()
