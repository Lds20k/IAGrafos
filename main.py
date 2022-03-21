import logging

import games.chess.main
import games.the_adventurer.main

logger_format = "%(name)s :: %(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(format = logger_format, encoding = 'utf-8', level = logging.INFO, handlers=[logging.StreamHandler()])

def main():
    #games.chess.main.start()
    games.the_adventurer.main.start()
    return 0

if __name__ == "__main__":
    main()
