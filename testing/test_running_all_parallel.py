import subprocess

if __name__ == '__main__':
    erase_process = subprocess.Popen(['coverage', 'erase'],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    erase_process.wait()

    run_test_suite_process = subprocess.Popen(['coverage', 'run', 'test_endpoint_dynamically_2.py'],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    run_test_suite_process.wait()

    # stdout,stderr = out.communicate()
    # print(stdout)

    xml_report_process = subprocess.Popen(['coverage', 'xml'],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    status_code = xml_report_process.wait()

    f = open("coverage.xml", "r")
    contents = f.read()
    print (contents)

    # stdout,stderr = out.communicate()
    print(status_code)
    print("Finalllllllll neaaaaaaaaaaaaaaa")
