from pkg_resources import parse_requirements
from setuptools import setup

NAME = 'scale-board'
DESCRIPTION = 'Displaying weight data on a remote display'
MODULES = ['scale_board', 'scale_board.settings', 'scale_board.board', 'scale_board.board.serial']

with open(file='VERSION', mode='r', encoding="UTF-8") as version_file:
    VERSION = version_file.read().replace("v", "")


def load_requirements(filename: str) -> list:
    with open(filename, 'r', encoding="utf-8") as file:
        return [f"""{req.name}{f"[{','.join(req.extras)}]" if req.extras else ''}{req.specifier}"""
                for req in parse_requirements(file.read())]


setup(
    name=NAME,
    version=VERSION,
    packages=MODULES,
    url='https://git.fkinuo.ru/scale-board',
    license='AGPL-3.0',
    author='Firin Kinuo',
    author_email='deals@fkinuo.ru',
    description=DESCRIPTION,
    install_requires=load_requirements('requirements.txt'),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'scale-board = scale_board.__main__',
        ]
    },
)
