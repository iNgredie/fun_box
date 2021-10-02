import re
import redis
from django.conf import settings

# extract domain from url
REG_EX = '^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/?\n]+)'

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


def get_domain(url: str) -> str:
    domain = re.match(REG_EX, url).group(1)
    return domain
