from typing import Callable

from catalyst.callbacks.metric import BatchMetricCallback
from catalyst.metrics._functional_metric import BatchFunctionalMetric


class FunctionalMetricCallback(BatchMetricCallback):
    """Custom metric in functional way.
    Note: the loader metrics calculated as average over all examples.

    Args:
        input_key: input key, specifies our `predictions`
        target_key: output key, specifies our `y_pred`
        metric_function: metric function, that get outputs, targets and return score as
        torch.Tensor
        prefix: key for the metric's name
    """

    def __init__(
        self, input_key: str, target_key: str, metric_function: Callable, prefix: str,
    ):
        """Init."""
        super().__init__(
            metric=BatchFunctionalMetric(metric_fn=metric_function, prefix=prefix),
            input_key=input_key,
            target_key=target_key,
        )


__all__ = ["FunctionalMetricCallback"]