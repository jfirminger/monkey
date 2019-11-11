from monkey.application import Server
import argparse
import logging
import sys, os

logger = logging.getLogger(__name__)

def main():
    LOG_FORMAT = (
        "%(asctime)s - %(name)s:%(funcName)s:%(lineno)s - %(levelname)s:  %(message)s"
    )
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    logger.info("Starting service.py:main")

    sys.path.append(os.getcwd())

    parser = argparse.ArgumentParser()
    parser.add_argument("--model-name", type=str, help="Name of the user model.")
    parser.add_argument("--workers", type=int, default=1, help="Number of workers.")
    parser.add_argument("--port", type=int, default=5000, help="Port to expose")

    args = parser.parse_args()

    options = {
                    "bind": "{}:{}".format("0.0.0.0", args.port),
                    "loglevel": "info",
                    "timeout": 5000,
                    "reload": "true",
                    "workers": args.workers
                } 
    Server(args.model_name, options).run()

if __name__ == "__main__":
    main()