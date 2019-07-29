from swagger_parser import SwaggerParser

from testing.NumberGen import NumberGen
from testing.Testing import Testing
from testing.Cat import Cat
from testing.Dog import Dog



def get_paths(parser):
    return parser.specification["paths"]


def process_params(id):

    # gen = NumberGen(1, 1, 10)
    # n = 0
    # while n != id:
    #     n = gen.mutate()
    #     print(n)

    parser = SwaggerParser(swagger_path='swagger/swagger.json')
    paths = get_paths(parser)

    paths_dict = {}

    # Iterating over all paths
    for path, info in paths.items():

        print(path)

        verbs_dict = {}
        # Iterating over all verbs
        for verb, value in info.items():
            str(verb)
            paramList = value["parameters"]

            genes_list = []
            for param in paramList:
                name = param["name"]
                required = param["required"]
                type = param["type"]
                print(name + str(required) + type)

                if param["type"]  == 'integer':
                    numberGen = NumberGen(name, 0, int(param["minimum"]),int(param["maximum"]))
                    genes_list.append(numberGen)

            # Adding genes list to the verbs_dict
            verbs_dict[verb] = genes_list

        # Adding genes list to the verbs_dict
        paths_dict[path] = verbs_dict

        print(paths_dict)
    return paths_dict
