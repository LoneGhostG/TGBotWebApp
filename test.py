import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            'https://lg1447-tgbotwebapp-test-backend.serveo.net/api/user',
            params={'user_id': 123},
            headers={'authorization': 'qwerasdfzxcv12345678'}
            
        ) as response:
            print(await response.json())


if __name__ == '__main__':
    asyncio.run(main())
