# import os
# import redis
from fastapi import FastAPI
# from random import randint


app = FastAPI()

@app.get("/")
def read_root():
    return {"hello: world"}




# r = redis.from_url(os.getenv("REDISURL", "redis://127.0.0.1.6379"))


# def main():
#     name =  randint(69420,99999)
#     r.set(name, "abcds")

# if __name__  == "__main__":
#     main()



