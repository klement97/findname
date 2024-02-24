import logging

from elastic_transport import AiohttpHttpNode as ESAiohttpHttpNode
from elasticsearch import AsyncElasticsearch

logger = logging.getLogger(__name__)


class AiohttpHttpNode(ESAiohttpHttpNode):
    async def perform_request(self, *args, **kwargs):
        try:
            resp = await super().perform_request(*args, **kwargs)
            if self.session and not self.session.closed:
                logger.info("closing session")
                await self.session.close()
                self.session = None
        except Exception as e:
            logger.exception(e)
            raise e
        return resp


class Database:
    def __init__(self, address, config):
        self.client = AsyncElasticsearch([address], **config)
