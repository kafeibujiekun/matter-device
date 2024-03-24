from typing import Optional

class WebSocketRunnerHooks():
    def connecting(self, url: str):
        """
        This method is called when the websocket is attempting to connect to a remote.

        Parameters
        ----------
        url: str
            The url the websocket is trying to connect to.
        """
        pass

    def abort(self, url: str):
        """
        This method is called when the websocket connection fails and will not be retried.

        Parameters
        ----------
        url: str
            The url the websocket has failed to connect to.
        """
        pass

    def success(self, duration: int):
        """
        This method is called when the websocket connection is established.

        Parameters
        ----------
        duration: int
            How long it took to connect since the last retry, in milliseconds.
        """
        pass

    def failure(self, duration: int):
        """
        This method is called when the websocket connection fails and will be retried.

        Parameters
        ----------
        duration: int
            How long it took to fail since the last retry, in milliseconds.
        """
        pass

    def retry(self, interval_between_retries_in_seconds: int):
        """
        This method is called when the websocket connection will be retried in the given interval.

        Parameters
        ----------
        interval_between_retries_in_seconds: int
            How long we will wait before retrying to connect, in seconds.
        """
        pass
