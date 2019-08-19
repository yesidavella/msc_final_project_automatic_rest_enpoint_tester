import re
import configparser
import logging


def replace(string, dict_replacements):
    substrings = sorted(dict_replacements, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: dict_replacements[match.group(0)], string)


def load_possible_genes_values(target_file):
    with open(target_file, "r") as myfile:
        data = myfile.readlines()

        dic_numbers = {}
        dic_strings = {}
        dict_replacements = {"\'": "", "\"": ""}

        for elem in data:
            numbers_line_list = re.findall("\d*", elem)
            text_line_list = re.findall("\"[\w<>/]*\"|\'[\w<>/]*\'", elem)

            for possible_number in numbers_line_list:

                if possible_number.isdigit():
                    dic_numbers[possible_number] = float(possible_number)

            for possible_text in text_line_list:

                if not possible_text.isdigit():
                    clean_string = replace(possible_text, dict_replacements)
                    dic_strings[clean_string] = clean_string

    logging.info("Possible values for Numbers: {}".format(dic_numbers))
    logging.info("Possible values for Strings: {}".format(dic_strings))
    print(dic_numbers)
    print(dic_strings)
    return dic_numbers, dic_strings
