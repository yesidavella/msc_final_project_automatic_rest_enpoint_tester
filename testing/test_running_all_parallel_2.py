import subprocess

if __name__ == '__main__':
    erase_process = subprocess.Popen(['coverage', 'erase'],
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    erase_process.wait()

    run_test_suite_process = subprocess.Popen(['coverage', 'run', '--source=silver_test', 'test_endpoint_dynamically_2.py'],
                                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    run_test_suite_process.wait()

    console_coverage_report_process = subprocess.Popen(['coverage', 'report', '-m'],
                                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    status_code = console_coverage_report_process.wait()

    print("El codigo de estado es: " + str(status_code))
    stdout, stderr = console_coverage_report_process.communicate()
    print(stdout)
