import subprocess, swagger_interpreter, logging

if __name__ == '__main__':

    genes_dict = swagger_interpreter.get_genes_from_file()
    # print(genes_dict)

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

            print(genes_in_string_format)

            exec_list_params = ['coverage', 'run', '--source=main_endpoint', 'test_endpoint_dynamically.py', genes_in_string_format]
            run_test_suite_proc = subprocess.Popen(exec_list_params, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            run_test_suite_proc.wait()

            console_coverage_report_process = subprocess.Popen(['coverage', 'report', '-m'],
                                                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            stdout, stderr = console_coverage_report_process.communicate()
            print(stdout)
    #
    # status_code = console_coverage_report_process.wait()
    #
    # print("El codigo de estado es: " + str(status_code))
    # stdout, stderr = console_coverage_report_process.communicate()
    print("Finallll")
