import sys


# def main(argv):
#
#     formatted = param_caster(argv)
#     print(formatted)


def ger_params_as_tuple_list(argv):

    param_array = []
    exep_msg_parsing_params = "Exception occured while parsing parameters: {}"

    try:
        only_params = argv[1:]
        param_pairs = only_params[0].strip().split(",")

        for index, param in enumerate(param_pairs):
            key, value = param.strip().split("=")
            param_array.append((str(index), key, value))

    except IndexError as e:
        print(exep_msg_parsing_params.format(str(e)))
        sys.exit(2)
    except Exception:
        print(exep_msg_parsing_params.format(Exception))

    return param_array


def get_coverage_metrics(bytes_object):
    cov_metrics_dict = {}

    string_cov_info = bytes_object.decode().splitlines()
    # 'Name          Stmts   Miss  Cover   Missing'
    title_array = string_cov_info[0].strip().split(" ")
    value_array = string_cov_info[2].strip().split("  ")

    clear_title_array = clear_array_of_spaces(title_array)
    clear_value_array = clear_array_of_spaces(value_array)

    for index, title in enumerate(clear_title_array):
        cov_metrics_dict[title] = clear_value_array[index]

    #set_pending_lines_as_array()
    missing_lines_one_by_one_dict = {}
    missing_lines_in_segments = cov_metrics_dict["Missing"].split(",")

    for line_segment in missing_lines_in_segments:

        if "-" in line_segment:
            bounds = line_segment.split("-")
            left_bound = int(bounds[0])
            right_bound = int(bounds[1])

            i = left_bound
            while i <= right_bound:
                missing_lines_one_by_one_dict[i] = i
                i += 1
        else:
            missing_lines_one_by_one_dict[int(line_segment.strip())] = int(line_segment.strip())

    cov_metrics_dict["detail_missing_lines"] = missing_lines_one_by_one_dict

    return cov_metrics_dict


def get_coverage_percentage(cov_metrics_dict):
    cov_percentage = cov_metrics_dict["Cover"]
    return int(cov_percentage.replace("%", ""))


def clear_array_of_spaces(dirty_array):

    clean_title_list = []
    for index, title in enumerate(dirty_array):
        if title.strip() != "":
            clean_title_list.append(title.strip())

    return clean_title_list


# if __name__ == "__main__":
#     main(sys.argv)

# param1=valueParam1,param2=valueParam2,param3=valueParam3
