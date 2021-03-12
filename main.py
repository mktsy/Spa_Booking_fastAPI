import uvicorn

# define an entry point for tunning the application.
if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", reload=True)
