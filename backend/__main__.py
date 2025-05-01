from fastapi import FastAPI
from utils.config import config

app = FastAPI()

if __name__ == '__main__':
    print('Backend Started!')
