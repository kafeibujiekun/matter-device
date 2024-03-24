import asyncio
import time
from abc import ABC, abstractmethod
from asyncio import CancelledError
from dataclasses import dataclass, field

class TestRunnerBase(ABC):
    """
    TestRunnerBase is an abstract interface that defines the set of methods a runner
    should implement.

    A runner is responsible for executing a test step.
    """
    @abstractmethod
    async def start(self):
        """
        This method is called before running the steps of a particular test file.
        It may allow the runner to perform some setup tasks.
        """
        pass

    @abstractmethod
    async def stop(self):
        """
        This method is called after running the steps of a particular test file.
        It may allow the runner to perform some cleanup tasks.
        """
        pass

    @abstractmethod
    async def execute(self, request):
        """
        This method executes a request using the adapter format, and returns a response
        using the adapter format.
        """
        pass

    @abstractmethod
    def run(self) -> bool:
        """
        This method runs a test suite.

        Returns
        -------
        bool
            A boolean indicating if the run has succeeded.
        """
        pass

    # @abstractmethod
    # def run(self, parser_builder_config: TestParserBuilderConfig, runner_config: TestRunnerConfig) -> bool:
    #     """
    #     This method runs a test suite.

    #     Returns
    #     -------
    #     bool
    #         A boolean indicating if the run has succeeded.
    #     """
    #     pass


class TestRunner(TestRunnerBase):
    async def start(self):
        return

    async def execute(self, request):
        return request

    async def stop(self):
        return

    async def run(self):
        result = await self._run_with_timeout()
        if isinstance(result, Exception) or isinstance(result, CancelledError):
            raise (result)
        elif not result:
            return False

        return True

    async def _run_with_timeout(self):
        await self.start()
        status = True
        return status
        # try:
        #     await self.start()
        #     status = await asyncio.wait_for(self._run(parser, config), parser.timeout)
        # except (Exception, CancelledError) as exception:
        #     status = exception
        # finally:
        #     if config.auto_start_stop:
        #         await self.stop()
        #     return status

    # async def _run(self, parser: TestParser, config: TestRunnerConfig):
    #     status = True
    #     try:
    #         hooks = config.hooks
    #         hooks.test_start(parser.filename, parser.name, parser.tests.count)

    #         test_duration = 0
    #         for idx, request in enumerate(parser.tests):
    #             if not request.is_pics_enabled:
    #                 hooks.step_skipped(request.label, request.pics)
    #                 continue
    #             elif not config.adapter:
    #                 hooks.step_start(request)
    #                 hooks.step_unknown()
    #                 continue
    #             elif config.pseudo_clusters.is_manual_step(request):
    #                 hooks.step_start(request)
    #                 await hooks.step_manual()
    #                 continue
    #             else:
    #                 hooks.step_start(request)

    #             start = time.time()
    #             if config.pseudo_clusters.supports(request):
    #                 responses, logs = await config.pseudo_clusters.execute(request, parser.definitions)
    #             else:
    #                 encoded_request = config.adapter.encode(request)
    #                 encoded_response = await self.execute(encoded_request)
    #                 responses, logs = config.adapter.decode(encoded_response)
    #             duration = round((time.time() - start) * 1000, 2)
    #             test_duration += duration

    #             logger = request.post_process_response(responses)

    #             if logger.is_failure():
    #                 hooks.step_failure(logger, logs, duration,
    #                                    request, responses)
    #             else:
    #                 hooks.step_success(logger, logs, duration, request)

    #             if logger.is_failure() and config.options.stop_on_error:
    #                 status = False
    #                 break

    #             if logger.warnings and config.options.stop_on_warning:
    #                 status = False
    #                 break

    #             if (idx + 1) == config.options.stop_at_number:
    #                 break

    #             if config.options.delay_in_ms:
    #                 await asyncio.sleep(config.options.delay_in_ms / 1000)

    #     except Exception as exception:
    #         status = exception
    #     finally:
    #         return status
