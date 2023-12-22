"""Скрипт для асинхронной обкачки урлов"""
import asyncio
import argparse
import aiohttp


async def fetch_url(session, url):
    """Запрос"""
    async with session.get(url) as response:
        return await response.text()


async def fetch_urls(urls):
    """Создание сеанса и задач"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        for url, response in zip(urls, responses):
            if isinstance(response, Exception):
                print(f"Failed to fetch {url}: {response}")
            else:
                print(f"Fetched {url}: {response[:50]}")


def main():
    """Главная функция"""
    parser = argparse.ArgumentParser(description='Async URL fetcher')
    parser.add_argument('concurrent_requests', type=int,
                        help='Number of concurrent requests')
    parser.add_argument('urls_file', type=argparse.FileType('r'),
                        help='File containing URLs')
    args = parser.parse_args()

    urls = [url.strip() for url in args.urls_file.readlines()]

    asyncio.run(fetch_urls(urls))


if __name__ == "__main__":
    main()
