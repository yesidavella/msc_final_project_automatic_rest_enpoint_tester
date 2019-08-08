import getopt
import sys


def main(argv):

    formatted = param_caster(argv)
    print(formatted)


def param_caster(argv):

    param_array = []
    exep_msg_parsing_params = "Exception occured while parsing parameters: {}"

    try:
        only_params = argv[1:]
        param_pairs = only_params[0].strip().split(",")

        for param in param_pairs:
            key, value = param.strip().split("=")
            param_array.append((key, value))

    except IndexError as e:
        print(exep_msg_parsing_params.format(str(e)))
        sys.exit(2)
    except Exception:
        print(exep_msg_parsing_params.format(Exception))

    return param_array


if __name__ == "__main__":
    main(sys.argv)

# param1=valueParam1,param2=valueParam2,param3=valueParam3
