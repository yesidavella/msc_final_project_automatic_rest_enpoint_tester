from flask import Flask, request

import unittest


app = Flask(__name__, instance_relative_config=True)


class SilverTest:

    @app.route('/basic/<id>', methods=['GET'])
    def basic_get(id):
        print("valor de id:" + str(id))
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

            status_code = 305
            answ = "All process carried out completely - basic_get()"


        json_response = app.response_class(
            response=answ,
            status=status_code,
            mimetype='application/json'
        )

        return json_response
        # return "hello"

    # def init(self):
    #     if __name__ == '__main__':
    #         app.run(host='0.0.0.0', port=8484, debug=True)


# def main():
#     # silver = SilverTest()
#     # silver.init()
#
#
#     app.testing = True
#     client = app.test_client()
#
#     with client:
#         rv = client.get('/basic/45', query_string={'param': 'ccccccccccc'})
#
#         # rv = c.get('/?vodka=42')
#         # # print( request.args['id'] )
#
#         print(rv._status)
#         # silver.basic_get()
#         # print(client)
# main()