"""Реализация сервера для приложения"""
import socket
import sys
import threading
import queue
import json
from collections import Counter
from urllib.request import urlopen
from bs4 import BeautifulSoup
from utils import IP, PORT, console_server, setup_logger

logger_server = setup_logger('second_logger', 'server_logfile.log')


class Server:
    """Сервер"""
    def __init__(self, num_workers, num_top_words):
        """Инициализация"""
        logger_server.info("__INIT__")
        self._num_workers = num_workers
        self._num_top_words = num_top_words
        self._num_handled_urls = 0
        self._client = 0
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((IP, PORT))
        self.server.listen(num_workers)
        self._que = queue.Queue(110)
        self._cnt = Counter()
        self._threads = [
            threading.Thread(
                target=self.handle_url,
                args=(),
                name=f"{i} Th"
            )
            for i in range(num_workers)
        ]

    def start(self):
        """Установка соединения с сервером и запуск потоков"""
        while True:
            self._client, address = self.server.accept()
            print(f"Connection Established - {address[0]}:{address[1]}")
            logger_server.info("__Start Threads")

            for thread in self._threads:
                thread.start()

            while True:
                try:
                    logger_server.info(
                        "Input_ Queue size: %s",
                        self._que.qsize()
                    )
                    url = self._client.recv(1024).decode("utf-8")
                except Exception:
                    continue

                self.divide_glued_urls(url)

    def divide_glued_urls(self, glued_urls: str) -> str:
        """"Создание очереди URL-адресов"""
        glued_urls = glued_urls.replace("\n", "")
        http_start = glued_urls.find("http")
        http_end = glued_urls[1:].find("http")

        while http_start != -1:
            if http_end == -1:
                url = glued_urls[:]
                self._que.put(url)
                break

            url = glued_urls[:http_end + 1]
            http_start = http_end + 1
            glued_urls = glued_urls[http_start:]
            http_end = glued_urls[1:].find("http")
            self._que.put(url)

    def handle_url(self):
        """Обработка URL-адресов"""
        wait = 0

        while True:
            logger_server.info(
                "__Handle th ::%s::",
                threading.current_thread().name
            )

            try:
                wait += 1
                url = self._que.get(timeout=1)
                wait = 0
                logger_server.info("__Correct url: %s", url)

            except Exception:
                logger_server.info("__Wait new url: %s", wait)
                if wait == 5:
                    logger_server.info(
                        "__Stop th ::%s::",
                        threading.current_thread().name
                    )
                    break
                continue

            text = self.get_text_from_url(url)
            lock = threading.Lock()

            with lock:
                self._cnt.update(text)
                self._num_handled_urls += 1
                logger_server.info(
                    "Handled Amount of URLS: %s",
                    self._num_handled_urls
                )
                print(f"Handled Amount of URLS: {self._num_handled_urls}")
                self.handle_requests()

    def get_text_from_url(self, url):
        """Извлечение текста с веб-страницы по URL-адресу"""
        with urlopen(url) as open_url:
            html = open_url.read()
        soup = BeautifulSoup(html, 'html.parser')

        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text()

        lines = (line.strip() for line in text.splitlines())
        chunks = (
            phrase.strip() for line in lines for phrase in line.split("  ")
        )
        text = '\n'.join(chunk for chunk in chunks if chunk).split()
        return text

    def handle_requests(self):
        """Нахождение наиболее часто встречающихся слов"""
        words = self._cnt.most_common(self._num_top_words)
        json_string = json.dumps(words, ensure_ascii=False)
        logger_server.info("__Send Answer: %s", json_string)
        self._client.send(bytes(json_string, "utf-8"))

    def que(self):
        """Возвращение значения атрибута"""
        return self._que

    def cnt(self):
        """Возвращение значения атрибута"""
        return self._cnt

    def num_workers(self):
        """Возвращение значения атрибута"""
        return self._num_workers

    def num_top_words(self):
        """Возвращение значения атрибута"""
        return self._num_top_words

    def num_handled_urls(self):
        """Возвращение значения атрибута"""
        return self._num_handled_urls

    def client(self):
        """Возвращение значения атрибута"""
        return self._client

    def threads(self):
        """Возвращение значения атрибута"""
        return self._threads


if __name__ == "__main__":
    parser = console_server()
    server_input = parser.parse_args(sys.argv[1:])
    object_server = Server(server_input.w, server_input.k)
    object_server.start()
