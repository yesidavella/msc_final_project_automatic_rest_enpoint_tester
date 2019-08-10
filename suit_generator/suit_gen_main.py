import logging
import subprocess
import swagger_interpreter
import parameter_caster

logging.basicConfig(filename='../logs/suit_gen_main.log', level=logging.DEBUG)

if __name__ == '__main__':

    genes_dict = swagger_interpreter.get_genes_from_file()

    for path_key, path_value in genes_dict.items():

        for verbs_name, gen_list in path_value.items():

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
            print(genes_in_string_format + " Verb name:" + verbs_name)

            exec_list_params = ['coverage', 'run', '--source=endpoint', 'dynamic_tester.py', genes_in_string_format]
            run_test_suite_proc = subprocess.Popen(exec_list_params, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            run_test_suite_proc.wait()

            console_coverage_report_process = subprocess.Popen(['coverage', 'report', '-m'],
                                                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            stdout, stderr = console_coverage_report_process.communicate()
            coverage_metrics_dict = parameter_caster.get_coverage_percentage(stdout)

            print(str(coverage_metrics_dict))

            erase_process = subprocess.Popen(['coverage', 'erase'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            erase_process.wait()
