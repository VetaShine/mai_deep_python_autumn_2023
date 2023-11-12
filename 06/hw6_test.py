"""Тестирование классов Client и Server"""
import unittest
import socket
import threading
import logging
import queue
from collections import Counter
from client import Client
from server import Server


class TestClient(unittest.TestCase):
    """Тестирование класса Client"""
    def setUp(self):
        """Создание временного сервера для тестирования и клиента"""
        self.server_address = ('localhost', 8888)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(self.server_address)
        self.server.listen()

        self.urls = ['http://www.example1.com', 'http://www.example2.com']
        self.number = 2
        self.client = Client(self.urls, self.number)

    def tearDown(self):
        """Остановка соединения сервера после тестов"""
        self.server.close()

    def test_init(self):
        """Тестирование клиента"""
        self.assertIsNotNone(self.client.server)
        self.assertEqual(self.client.urls_file(), self.urls)
        self.assertEqual(self.client.num_threads(), self.number)
        self.assertEqual(len(self.client.threads), self.number)
        for thread in self.client.threads:
            self.assertIsInstance(thread, threading.Thread)


class TestServer(unittest.TestCase):
    """Тестирование класса Server"""
    def setUp(self):
        """Создание временного сервера для тестирования"""
        self.ip = 'localhost'
        self.port = 8888
        self.num_workers = 10
        self.num_top_words = 5
        self.server = Server(self.num_workers, self.num_top_words)
        self.server.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.server.setsockopt(socket.SOL_SOCKET,
                                      socket.SO_REUSEADDR, 1)
        self.server.server.bind((self.ip, self.port))
        self.server.server.listen(self.num_workers)

    def tearDown(self):
        """Остановка соединения сервера после тестов"""
        self.server.server.close()

    def test_init(self):
        """Тестирование сервера"""
        self.assertEqual(self.server.num_workers(), self.num_workers)
        self.assertEqual(self.server.num_top_words(), self.num_top_words)
        self.assertEqual(self.server.num_handled_urls(), 0)
        self.assertEqual(self.server.client(), 0)
        self.assertIsInstance(self.server.server, socket.socket)
        self.assertIsInstance(self.server.que(), queue.Queue)
        self.assertIsInstance(self.server.cnt(), Counter)
        self.assertEqual(len(self.server.threads()), self.num_workers)
        for i, thread in enumerate(self.server.threads()):
            self.assertIsInstance(thread, threading.Thread)
            self.assertEqual(thread.name, f"{i} Th")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
