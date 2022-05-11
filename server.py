from flask import Flask
app = Flask(__name__)
import conectionDB

rows = conectionDB.connecion()

usuarios = {}
cont = 1
body = ''
for row in rows:
    usuarios['row_' + str(cont)] = {'person_id': row[0],
                        'firstName': row[1],
                        'lastName': row[2],
                        'address': row[3]}
    body += '<div style="border: 3px solid black; background-color: red; color: white; margin: 4px 0;">' + 'IdPersona: ' + str(row[0]) + ' | firstName:' + row[1] + ' | lastName:' + row[2] + ' | adress:' + row[3] + '</div>'
    cont+=1


@app.route('/')
def hello_world():
    return body

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, ssl_context=('cert.pem', 'key.pem'))