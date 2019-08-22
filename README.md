[![](https://www.tpdegrees.com/wp-content/uploads/2019/05/QMUL-logo-600-575x338.png)](https://www.tpdegrees.com/wp-content/uploads/2019/05/QMUL-logo-600-575x338.png)
# REST ENDPOINT PARAMETER VALUE GENERATOR OF TEST CASES USING COVERAGE AS MAIN METRIC
It is a component which was capable of creating in automatic or at least in semi-automatic way test suites (a set of test cases) of endpoints. Usually, developers are reluctant to develop them because it implies more complexity involved in the process as well time consumed. It is required to boost the process of “Continuous Delivery” and “Continuous Integration”, and Unit Testing is a useful tool to achieve those goals in the modern software industry.

> The artefact will be developed in Python to generate test cases of Python endpoints implementations.

Only GET and DELETE methods will be covered in the proposal. As it was exposed, REST APIs usually are developed with four methods (GET, PUT, POST and DELETE). When the “request” is done in the client-server architecture, the methods GET and DELETE do not have any payload, they have (in a simplified way) the URL and some parameters used later to either get the representation of the resource or to delete it. Therefore, this proposal will just embrace GET and DELETE methods; any other information like Headers and similar metadata will not be considered either. 

## Getting Started

1. Download the project from  https://github.com/yesidavella/agenetic_rest_tester.git previous allowance given by the author.
2. Install Python 3.7
3. Install coverage as dependency in Python environment
4. local_project_folder/suit_generator$ python suit_gen_main.py 
Then, you will see
[http://github.com/yesidavella/agenetic_rest_tester/blob/master/executing.png](http://github.com/yesidavella/agenetic_rest_tester/blob/master/executing.png)
It means that the project is running and testing and endpoint to find the optimal unit test suite.

### Prerequisites and Installing
The next instructions are given to linux operating system

1. It is required Python 3.6 or newer
```
sudo apt install python3.7
```
2. It is required coverage library
```
$ pip install coverage
```
## Running the scenario

> **NOTE**: It is exercising and testing the functional enpoint located in local_folder_project/suit_generator/endpoint.py

An endpoint is again published in localhost:8484/basicget/{id} and receiving two additional parameters called limit and type. The first and third are strings and the second is an integer.

In a browser URL, it should be typed: localhost:8484/basicget/34?limit=33&type=hola to have the next answer showed in Figure 8 Basic endpoint invocation.

The endpoint has the next if-guarded blocks along with the code.
> In line 19 if id == "vip"
In line 24 if limit > 80
In line 29 if limit > 50 and id == "vip"
In line 34 if limit <= 10
In line 39 if 20 <= limit <= 40
In line 44 if type == "hello"

**Hypothesis**
It is required only three test cases with the parameter values to fulfil the if-guarded blocks and get complete coverage. 

> Test case1: id =”vip” and limit=81 and type=”hello” fulfilling if id == "vip",  if limit > 80, if limit > 50 and id == "vip" and if type == "hello". 

> Test case2: id =Any value, limit=10 and type=any value fulfilling if limit <= 10. 

> Test case3: id =Any value, limit=30 and type=any value fulfilling if 20 <= limit <= 40.

**Execution**
After 3 minutes of execution, it created three test cases with 
> id=vip, type=hello and limit=10
id=vip, type=hello and limit=40
id=vip, type=hello and limit=8484

It showed to be more efficient because with these values, it enters inside four if-guarded blocks.

**Conclusion**
The test suite generator achieved to prove the HYPOTESYS calculating a test suite of 3 tests to cover and go inside the if-guarded blocks. The maximum coverage was reached. 

## Authors

* **Yesid Andres Avella Ospina** - *Initial work* - [QMUL](https://github.com/yesidavella/)

## License

This project is licensed under GNU Lesser General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
I would like to express my sincere gratitude to my supervisor Dr Mustafa Bozkurt, for his continuous support of my MSc. project, especially for his patience and knowledge. His guidance helped me in all the time of research and writing of this dissertation.  

Moreover, I would like to thank all my friends, especially Anthony Maldonado in London and Franklin Martinez in Bogotá, whose advice was valuable in many of the difficult moments of this challenge. 

Last but not least, I would like to especially thank my mother Lelia Ospina, my beloved sister Laura Avella and father Luis Avella for always believing in me.
