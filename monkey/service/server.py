from monkey.service.application import PredictionServer
import argparse
import logging
import sys, os
import multiprocessing as mp


logger = logging.getLogger(__name__)

def run(application):
    """
    Start server
    """
    try:
        process = mp.Process(target=application)
        process.daemon = True
        process.start()
        process.join()
        
    except Exception as e:
        print(e)
        print("Could not start prediction service")

def prediction_server(model_name, options, wsgi_flag):
    """
    Returns callable prediction server 
    """
    return PredictionServer(model_name, options).run(wsgi_flag)

def main():
    LOG_FORMAT = (
        "%(asctime)s - %(name)s:%(funcName)s:%(lineno)s - %(levelname)s:  %(message)s"
    )
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

    sys.path.append(os.getcwd())

    parser = argparse.ArgumentParser()
    parser.add_argument("--model-name", type=str, help="Name of the user model.")
    parser.add_argument("--workers", type=int, default=1, help="Number of workers.")
    parser.add_argument("--port", type=int, default=5000, help="Port to expose")
    parser.add_argument('--wsgi', dest='wsgi_flag', action='store_true')
    parser.add_argument('--no-wsgi', dest='wsgi_flag', action='store_false')
    parser.set_defaults(wsgi_flag=True)
    args = parser.parse_args()

    options = {
                    "bind": "{}:{}".format("0.0.0.0", args.port),
                    "loglevel": "info",
                    "timeout": 5000,
                    "reload": "true",
                    "workers": args.workers
                } 
    application = prediction_server(args.model_name, options, args.wsgi_flag)
    run(application)

if __name__ == "__main__":
    main()