"""Тестирование скрипта для асинхронной обкачки урлов"""
import unittest
import aiohttp
from fetcher import fetch_urls


class Test(unittest.TestCase):
    """Класс тестирования"""
    async def test_fetch_urls(self):
        """Обкачка нескольких урлов"""
        urls = ['https://ru.pinterest.com', 'https://eda.ru']
        expected_output = ['<!doctype html>', '<!doctype html>']
        async with aiohttp.ClientSession():
            responses = await fetch_urls(urls)
            for response, expected in zip(responses, expected_output):
                self.assertIn(expected, response)

    async def test_fetch_urls_single_url(self):
        """Обкачка одного урла"""
        urls = ['https://www.google.com']
        expected_output = ['<!doctype html>']
        async with aiohttp.ClientSession():
            responses = await fetch_urls(urls)
            for response, expected in zip(responses, expected_output):
                self.assertIn(expected, response)


if __name__ == '__main__':
    unittest.main()
