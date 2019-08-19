import logging
import subprocess
import swagger_interpreter
import parameter_caster
import configparser


config = configparser.ConfigParser()
config.read('config.INI')
COVERAGE_TO_STOP = float(config['APP_PARAMS']['COVERAGE_TO_STOP'])

target_file = config['APP_PARAMS']['FILE_NAME_TO_GUESS_VALUES']

logging.basicConfig(filename='../logs/suit_gen_main.log', level=logging.DEBUG)


def mutual_elimination(new_dict, old_dict):

    temp_array = []
    for old_miss_line in old_dict:
        if old_miss_line in new_dict:
            item = new_dict.pop(old_miss_line)
            temp_array.append(item)

    for item in temp_array:
        old_dict.pop(item)

    for new_miss_line in new_dict:
        if new_miss_line in old_dict:
            old_dict.pop(new_miss_line)

    return new_dict, old_dict


def reset_optimal_set(opt_dict):
    for key in opt_dict:
        opt_dict[key][1] = False


if __name__ == '__main__':

    genes_dict = swagger_interpreter.get_genes_from_file(target_file)

    for path_key, path_value in genes_dict.items():

        for verbs_name, gen_list in path_value.items():

            current_cov_per = 0.0;

            dict_optimal_set = {}

            while COVERAGE_TO_STOP > current_cov_per:

                erase_process = subprocess.Popen(['coverage', 'erase'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                erase_process.wait()

                # Iteration over genes
                genes_in_string_format = ""

                for index, gen in enumerate(gen_list, start=1):
                    gen.mutate()
                    if index == len(gen_list):
                        genes_in_string_format += "%s=%s" % (gen.get_name(), gen.get_value())
                    else:
                        genes_in_string_format += "%s=%s," % (gen.get_name(), gen.get_value())

                logging.info("Suit_gen_main genes to invoke test {}".format(genes_in_string_format))
                # print(genes_in_string_format + " Verb name:" + verbs_name)

                exec_list_params = ['coverage', 'run', '--source=endpoint', 'dynamic_tester.py', genes_in_string_format]
                run_test_suite_proc = subprocess.Popen(exec_list_params, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                run_test_suite_proc.wait()

                console_coverage_report_process = subprocess.Popen(['coverage', 'report', '-m'],
                                                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                stdout, stderr = console_coverage_report_process.communicate()
                coverage_metrics_dict = parameter_caster.get_coverage_metrics(stdout)

                current_cov_per = parameter_caster.get_coverage_percentage(coverage_metrics_dict)

                if not bool(dict_optimal_set):
                    dict_optimal_set[path_key+verbs_name+genes_in_string_format] = [ coverage_metrics_dict["detail_missing_lines"], False]
                else:
                    add_to_opt = True;
                    for key in dict_optimal_set:

                        new_dict, old_dict = mutual_elimination(coverage_metrics_dict["detail_missing_lines"].copy(), dict_optimal_set[key][0].copy())

                        new_is_empty = not bool(new_dict)
                        old_is_empty = not bool(old_dict)

                        if (old_is_empty):
                            add_to_opt = False
                            break
                        elif new_is_empty and not old_is_empty:
                            dict_optimal_set[key][1] = True
                        elif not new_is_empty and not old_is_empty:
                            dict_optimal_set[key][1] = False

                    list_del_opt = []
                    for key in dict_optimal_set:
                        if dict_optimal_set[key][1]:
                            list_del_opt.append(key)

                    for key in list_del_opt:
                        dict_optimal_set.pop(key)

                    if add_to_opt:
                        dict_optimal_set[path_key+verbs_name+genes_in_string_format] = [coverage_metrics_dict["detail_missing_lines"], False]

                    reset_optimal_set(dict_optimal_set)


                print(str(dict_optimal_set))
                #print(path_key + verbs_name + genes_in_string_format + " Cove %: " + str(current_cov_per))
                # erase_process = subprocess.Popen(['coverage', 'erase'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                # erase_process.wait()
