"""Реализация клиента для приложения"""
import socket
import sys
import threading
from itertools import islice
from utils import IP, PORT, console_client, setup_logger

logger = setup_logger('first_logger', 'client_logfile.log')


class Client:
    """Клиент"""
    def __init__(self, urls, number) -> None:
        """Инииализация"""
        logger.info("__INIT__")
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._urls_file = urls
        self._num_threads = number

        self.threads = [
            threading.Thread(
                target=self.handle_request,
                args=(i,),
                name=f"{i} Th"
            )
            for i in range(self._num_threads)
        ]

    def connect(self):
        """Соединение с сервером"""
        logger.info("__Connect__")
        self.server.connect((IP, PORT))

        for thread in self.threads:
            logger.info("__start %s", thread)
            thread.start()

        for _ in range(100):
            answer = self.server.recv(1024).decode("utf-8")
            print(answer, end="\n\n")

    def handle_request(self, th_num):
        """Обработка URL-адреса из файла"""
        logger.info("__HANDLE_REQUEST__")
        lock = threading.Lock()

        with lock:
            with open(self._urls_file, "r", encoding='utf-8') as file_d:
                lines = islice(
                    file_d,
                    th_num * self._num_threads,
                    (th_num + 1) * self._num_threads
                )

                for url in lines:
                    logger.info(
                        "__send: %s: %s",
                        threading.current_thread().name,
                        url
                    )

                    self.server.send(bytes(url, "utf-8"))

    def urls_file(self):
        """Возвращение значения атрибута"""
        return self._urls_file

    def num_threads(self):
        """Возвращение значения атрибута"""
        return self._num_threads


if __name__ == "__main__":
    parser = console_client()
    client_input = parser.parse_args(sys.argv[1:])
    client = Client(client_input.f, client_input.m)
    client.connect()
