import uvicorn

appName = "ukid"
Host = "127.0.0.1"
Port = "8000"
uvicorn.run(appName+":app", host=Host, port=Port, log_level='info', access_log=False)