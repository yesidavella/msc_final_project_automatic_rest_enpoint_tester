
from flask import Flask, request
from testing.swagger_caster import process_params


app = Flask(__name__, instance_relative_config=True)


@app.route('/test/<id>')
def test(id):
    result = request.args.get("name", "correctly!!!")
    paths_with_genes = process_params(id)

    return '<h1>Silver bullet working, {}</h1>'.format(result)


@app.route('/basic/<id>', methods=['GET'])
def basic_get(id):

    print("Calling /basic/<id>. Printing request: " + str(request))

    answ = None
    status_code = None

    if type(id) is not int:
        id = int(id)

    if id <= 0:
        status_code = 400
        answ = "Invalid id less or equal to 0, use id number greater than 0"
    else:

        print("Beginning complete process of basic_get()")
        print("Querying DB - basic_get()")
        print("Checking queues - basic_get()")

        status_code = 200
        answ = "All process carried out completely - basic_get()"


    json_response = app.response_class(
        response=answ,
        status=status_code,
        mimetype='application/json'
    )

    return json_response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8484, debug=True)
