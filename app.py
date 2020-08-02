#!/usr/bin/env python3

import subprocess

from flask import Flask, jsonify
from rq import Queue
from rq.job import Job
from worker import conn

import musescore

app = Flask(__name__)

q = Queue(connection=conn)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/version')
def version():
    v = subprocess.check_output(['mscore3', '--version'])
    return v
@app.route('/convert')
def convert():
    file = 'TonBaleArGoz.mscz'
    result = q.enqueue(musescore.convert, file)
    app.logger.info(f"Job: {result.id} / File: {file}")
    return result.id


@app.route("/results/<job_key>", methods=['GET'])
def get_results(job_key):

    job = q.fetch_job(job_key)

    if job.is_finished:
        app.logger.info("testtest")
        app.logger.info(job.result)
        return jsonify(job.result)
    else:
        return "Nay!", 202

if __name__ == "__main__":
    app.run(host='0.0.0.0')