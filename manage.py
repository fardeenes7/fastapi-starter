if __name__ == "__main__":
    from api.index import app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)