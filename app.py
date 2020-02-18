import web
import json
import app

class estudiantes_url :
    def GET(self):
        try:
            data=web.input()
            if data['token'] == '1234':
                student1=(data['student1'])
        