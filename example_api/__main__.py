import argparse
import asyncio
import os
from pathlib import Path

from example_api import logging, __version__
from example_api.config import Config


def parse_args(args):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.MetavarTypeHelpFormatter)

    parser.add_argument('-v',
                        '--version',
                        action="version",
                        version="%(prog)s " + __version__)

    parser.add_argument("-d",
                        "--debug",
                        action="store_true",
                        help="Enables DEBUG level logging")

    parser.add_argument(
        "--config-file",
        type=Path,
        default=os.environ.get('EXAMPLE_API_CONFIG'),
        help=
        "A json/toml/yml config containing settings used to configure this service (default: example_api_CONFIG envvar)"
    )

    parser.add_argument(
        "--bind",
        dest="server.address",
        type=str,
        default="0.0.0.0:9080",
        help="Where this application will be bound [%(default)s]")

    parser.add_argument("--reload",
                        dest="server.reload",
                        action="store_true",
                        help="Enables hot-reloading")

    return parser.parse_args(args)


def main(args=None):
    logging.install()
    args = parse_args(args)

    if args.debug:
        logging.setLevel("DEBUG")
        asyncio.get_event_loop().set_debug(True)

    config = Config({k: v for k, v in vars(args).items() if k != 'func'})

    if 'EXAMPLE_API_CONFIG' in os.environ:
        config.load(os.environ['EXAMPLE_API_CONFIG'])

    elif args.config_file:
        os.environ['EXAMPLE_API_CONFIG'] = str(args.config_file)
        config.load(args.config_file)

    for key, value in config.items():
        if key.startswith('logging.'):
            logging.setLevel(value, key[8:])

    from example_api import server
    server.start(config)


if __name__ == "__main__":
    main()