from typing import Callable

from tonclient.decorators import result_as
from tonclient.module import TonModule
from tonclient.types import ParamsOfQuery, ResultOfQuery, \
    ParamsOfQueryCollection, ResultOfQueryCollection, \
    ParamsOfWaitForCollection, ResultOfWaitForCollection, \
    ResultOfSubscribeCollection, ParamsOfSubscribeCollection


class TonNet(TonModule):
    """ Free TON net SDK API implementation """
    @result_as(classname=ResultOfQueryCollection)
    def query_collection(
            self, params: ParamsOfQueryCollection) -> ResultOfQueryCollection:
        """
        Queries collection data.
        Queries data that satisfies the `filter` conditions, limits the number
        of returned records and orders them. The projection fields are limited
        to result fields
        :param params: See `types.ParamsOfQueryCollection`
        :return: See `types.ResultOfQueryCollection`
        """
        return self.request(method='net.query_collection', **params.dict)

    @result_as(classname=ResultOfWaitForCollection)
    def wait_for_collection(
            self, params: ParamsOfWaitForCollection
    ) -> ResultOfWaitForCollection:
        """
        Returns an object that fulfills the conditions or waits for its
        appearance. Triggers only once.
        If object that satisfies the `filter` conditions already exists -
        returns it immediately. If not - waits for insert/update of data
        within the specified `timeout`, and returns it. The projection fields
        are limited to `result` fields
        :param params: See `types.ParamsOfWaitForCollection`
        :return: See `types.ResultOfWaitForCollection`
        """
        return self.request(method='net.wait_for_collection', **params.dict)

    @result_as(classname=ResultOfSubscribeCollection)
    def subscribe_collection(
            self, params: ParamsOfSubscribeCollection,
            callback: Callable = None
    ) -> ResultOfSubscribeCollection:
        """
        Creates a subscription.
        Triggers for each insert/update of data that satisfies the `filter`
        conditions. The projection fields are limited to `result` fields
        :param params: See `types.ParamsOfSubscribeCollection`
        :param callback: Additional responses handler
        :return:
        """
        return self.request(
            method='net.subscribe_collection', callback=callback,
            **params.dict)

    def unsubscribe(self, params: ResultOfSubscribeCollection):
        """
        Cancels a subscription.
        Cancels a subscription specified by its handle
        :param params: See `types.ResultOfSubscribeCollection`
        """
        return self.request(method='net.unsubscribe', **params.dict)

    @result_as(classname=ResultOfQuery)
    def query(self, params: ParamsOfQuery) -> ResultOfQuery:
        """
        Performs DAppServer GraphQL query
        :param params: See `types.ResultOfQuery`
        :return: See `types.ResultOfQuery`
        """
        return self.request(method='net.query', **params.dict)

    def suspend(self):
        """ Suspends network module to stop any network activity """
        return self.request(method='net.suspend')

    def resume(self):
        """ Resumes network module to enable network activity """
        return self.request(method='net.resume')
