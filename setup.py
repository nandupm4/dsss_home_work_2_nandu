from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    description='A simple math quiz game',
    author='Nandu',
    author_email='nandu.manoj@fau.de',
    packages=find_packages(),
    install_requires=[],  
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',  # The command to run the main function
        ],
    },
)
