import os
import requests
import datetime
import json
from flask import Flask, render_template, make_response, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Index(Resource):
    def post(self, company):
        '''Post logs to server'''
        if os.path.isdir("logs/{}".format(company)) == False:
            os.mkdir("logs/{}".format(company))
        
        date = str(datetime.datetime.now()).split()
        empty = ""
        newDate = empty.join(date)

        logFile = open("logs/{}/{}{}.log".format(company, company, newDate), "w+")
        logFile.write(request.data.decode("utf-8"))

        return {201: "OK"}

api.add_resource(Index, "/<string:company>")