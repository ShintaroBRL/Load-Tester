# Load Test
> program developed for load testing on certain sites, the program is NOT universal and will require modifications for each site that will be used

[![Build Status][build-button]][build]
[![Latest Version][mdversion-button]][md-pypi]
[![Python Versions][pyversion-button]][md-pypi]

program developed for AUTHORIZED TESTS this tool was NOT developed with the intention of leaving sites down

## Installation

OS X & Linux:

```sh
pip install -y pyfiglet clint argparse requests
```

## Usage example

Just run the command below after installing the necessary libraries, make sure you have access to the internet for the program to work correctly. It is recommended to use this program observing the server status

```sh
python LoadTest.py --url (http://mysite/login.html) --ssl (true/false) --logs (true/false) --users (100) --sleep (0.5)
```

## Development setup

Required Libs:

```sh
pip install -y pyfiglet clint argparse requests
```


## Meta

Juliano Lira Florentino –  juliano0forum@gmail.com

Distributed under the GNU GENERAL PUBLIC LICENSE license. See ``LICENSE`` for more information.

[https://github.com/ShintaroBRL/Load-Tester/blob/master/LICENSE](https://github.com/ShintaroBRL)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[build-button]: https://github.com/Python-Markdown/markdown/workflows/CI/badge.svg?event=push
[build]: https://github.com/Python-Markdown/markdown/actions?query=workflow%3ACI+event%3Apush
[mdversion-button]: https://img.shields.io/pypi/v/Markdown.svg
[md-pypi]: https://pypi.org/project/Markdown/
[pyversion-button]: https://img.shields.io/pypi/pyversions/Markdown.svg