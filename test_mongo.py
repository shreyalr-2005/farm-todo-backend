import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient

async def test_mongo():
    uri = os.environ.get("MONGODB_URI", "mongodb+srv://shravyashreya26_db_user:shreyaramesh_24@cluster0.5piwtma.mongodb.net/todo?appName=Cluster0")
    with open("error.log", "w") as f:
        f.write(f"Connecting to {uri}\n")
        try:
            # trying with certifi
            import certifi
            client = AsyncIOMotorClient(uri, tlsCAFile=certifi.where(), serverSelectionTimeoutMS=5000)
            res = await client.admin.command('ping')
            f.write(f"Success with certifi: {res}\n")
            return
        except Exception as e:
            f.write(f"Failed with certifi: {type(e).__name__} {str(e)}\n")

        try:
            # trying without certifi
            client = AsyncIOMotorClient(uri, tlsAllowInvalidCertificates=True, serverSelectionTimeoutMS=5000)
            res = await client.admin.command('ping')
            f.write(f"Success with tlsAllowInvalidCertificates: {res}\n")
            return
        except Exception as e:
            f.write(f"Failed with tlsAllowInvalidCertificates: {type(e).__name__} {str(e)}\n")

        try:
            # trying with certifi but with tlsAllowInvalidCertificates=True
            import certifi
            client = AsyncIOMotorClient(uri, tlsCAFile=certifi.where(), tlsAllowInvalidCertificates=True, serverSelectionTimeoutMS=5000)
            res = await client.admin.command('ping')
            f.write(f"Success with both: {res}\n")
            return
        except Exception as e:
            f.write(f"Failed with both: {type(e).__name__} {str(e)}\n")

asyncio.run(test_mongo())
