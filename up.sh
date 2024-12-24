#!/usr/bin/env bash

gunicorn -k uvicorn.workers.UvicornWorker app:app