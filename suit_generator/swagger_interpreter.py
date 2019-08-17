from swagger_parser import SwaggerParser
from StringGen import StringGen
from NumberGen import NumberGen
import possible_values_parser


def get_genes_from_file():

    parser = SwaggerParser(swagger_path='../swagger/swagger.json')
    paths = get_paths(parser)

    paths_dict = {}
    dict_poss_numbers, dict_poss_string = possible_values_parser.load_possible_genes_values()

    # Iterating over all paths (path is an structure in the swagger file)
    for path, info in paths.items():

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

                if param["type"] == 'integer':
                    numberGen = NumberGen(name, 0, int(param["minimum"]), int(param["maximum"]), dict_poss_numbers)
                    genes_list.append(numberGen)
                if param["type"] == 'string':
                    stringGen = StringGen(name, required, "", 3, dict_poss_string)
                    genes_list.append(stringGen)

            # Adding genes list to the verbs_dict
            verbs_dict[verb] = genes_list

        # Adding genes list to the verbs_dict
        paths_dict[path] = verbs_dict


    return paths_dict


def get_paths(parser):
    return parser.specification["paths"]
