from setuptools import setup, find_packages

setup(
    name='ai_defender',
    version='0.1',
    packages=find_packages(),
    description='مكتبة ذكاء اصطناعي لحماية الهاتف من الاختراق',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Ahmed mohammed',
    author_email='programmer2020dev@gmail.com',
    url='https://github.com/yourusername/ai_defender',
    keywords=['security', 'ai', 'mobile'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
