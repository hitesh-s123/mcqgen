from setuptools import find_packages,setup

setup(
    name = 'mcqgenerator',
    version='0.0.1',
    author='hitesh',
    author_email='jnvpghitesh@gmail.com',
    install_requires=['transformers','accelerate','tensorflow','tokenizers','langchain','streamlit','python-dotenv','PyPDF2','langchain_community','pydantic'],
    packages=find_packages()
)