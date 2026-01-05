import time
import functools
from typing import Callable, Any
import traceback


def log_execution_time(func: Callable) -> Callable:
    """関数の実行時間をログに出力するデコレーター"""

    @functools.wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        func_name = func.__name__

        try:
            # 関数の実行
            result = await func(*args, **kwargs)

            # 実行時間の計算とログ
            execution_time = time.time() - start_time
            logger.info(
                f"[{func_name}] completed successfully in {execution_time:.3f}s"
            )

            # 実行時間が長い場合は警告
            if execution_time > 5.0:
                logger.warning(
                    f"{func_name} took {execution_time:.3f}s - "
                    "consider optimizing the code"
                )

            return result

        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(
                f"{func_name} failed after {execution_time:.3f}s: {e}\n"
                f"Traceback:\n{traceback.format_exc()}"
            )
            raise

    return wrapper
