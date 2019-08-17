import logging
import subprocess
import swagger_interpreter
import parameter_caster
import configparser


config = configparser.ConfigParser()
config.read('config.INI')

# MUTATION_PERCENTAGE = int(config['GEN_ALG_PARAMS']['MUTATION_PERCENTAGE'])
# CHAMPIONS_AMOUNT = int(config['GEN_ALG_PARAMS']['CHAMPIONS_AMOUNT'])
# POPULATION_SIZE = int(config['GEN_ALG_PARAMS']['POPULATION_SIZE'])
# KEEP_CHAMPIONS_IN_NEW_GENERATION = config['GEN_ALG_PARAMS']['KEEP_CHAMPIONS_IN_NEW_GENERATION'] == 'True'

COVERAGE_TO_STOP = float(config['APP_PARAMS']['COVERAGE_TO_STOP'])

logging.basicConfig(filename='../logs/suit_gen_main.log', level=logging.DEBUG)

if __name__ == '__main__':

    genes_dict = swagger_interpreter.get_genes_from_file()

    for path_key, path_value in genes_dict.items():

        for verbs_name, gen_list in path_value.items():

            current_cov_per = 0.0;

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

                print(path_key + verbs_name + genes_in_string_format + " Cove %: " + str(current_cov_per))
                # erase_process = subprocess.Popen(['coverage', 'erase'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                # erase_process.wait()
