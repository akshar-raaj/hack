import logging

def main():
    d = {'a': 1, 'b': 2}
    logging.basicConfig(level=logging.INFO)
    logging.info("Hello")
    logging.info(d)

main()
