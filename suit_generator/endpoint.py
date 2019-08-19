from flask import Flask, request
import logging


app = Flask(__name__, instance_relative_config=True)


class DynamicTester:

    @app.route('/basicget/<id>', methods=['GET'])
    def basic_get(id):
        logging.info("Beginning call on /basicget/<id>. Printing request: {}".format(str(request)))

        answ = None
        status_code = None
        limit = request.args.get("limit", 0, type=int)

        if id == "vip":
            print("ID - Querying DB - opening...")
            print("ID - Querying DB - validating resultset")
            print("ID - Querying DB - setting some data")

        if limit > 80:
            print("limit - Validating limit...")
            print("limit - limits exceeds allowed boundary")
            print("limit - more stuff")

        if limit > 50 and id == "vip":
            print("ID and Limit - Mixed variables - opening...")
            print("ID and Limit - Mixed variables - doing something")
            print("ID and Limit - Mixed variables - last line")

        if limit <= 10:
            print("limit - Validating limit...")
            print("limit - limits exceeds allowed boundary")
            print("limit - more stuff")

        if 20 <= limit <= 40:
            print("limit - Validating limit...")
            print("limit - limits exceeds allowed boundary")
            print("limit - more stuff")


        print("Endpoint General stuff 1")
        print("Endpoint General stuff 2")
        print("Endpoint General stuff 3")

        status_code = 200
        answ = "All process carried out completely - request: {}".format(str(request))

        json_response = app.response_class(
            response=answ,
            status=status_code,
            mimetype='application/json'
        )

        logging.info("Finishing call on /basicget/<id>. Printing request: {}".format(str(request)))

        return json_response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8484, debug=True)
