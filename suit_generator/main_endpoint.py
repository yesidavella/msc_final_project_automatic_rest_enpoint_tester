from flask import Flask, request
import logging


app = Flask(__name__, instance_relative_config=True)
logging.basicConfig(filename='main_endpoint.log', level=logging.DEBUG)


@app.route('/basicget/<id>', methods=['GET'])
def basic_get(id):
    logging.basicConfig(filename='main_endpoint.log', level=logging.DEBUG)
    logging.info("argvxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Beginning call on /basicget/<id>. Printing request: {}".format(str(request)))

    answ = None
    status_code = None
    limit = request.args.get("limit", 0, type=int)

    if id == "vip":
        print("ID - Querying DB - opening...")
        print("ID - Querying DB - validating resultset")
        print("ID - Querying DB - setting some data")

    if limit > 100:
        print("limit - Validating limit...")
        print("limit - limits exceeds allowed boundary")
        print("limit - more stuff")

    print("General stuff 1")
    print("General stuff 2")

    status_code = 200
    answ = "All process carried out completely - request: {}".format(str(request))

    json_response = app.response_class(
        response=answ,
        status=status_code,
        mimetype='application/json'
    )

    return json_response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8484, debug=True)
