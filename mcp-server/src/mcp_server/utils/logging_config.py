import logging
import sys
from pathlib import Path
from datetime import datetime


def setup_logging(level="INFO", log_to_file=True):
    """ロギング設定を行う

    Args:
        level: ログレベル (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_to_file: ログをファイルに出力するかどうか
            True: ログをファイルに出力
            False: ログを標準出力に出力

    Returns:
        logging.Logger: 設定済ロギングオブジェクト
    """

    # ログディレクトリの作成
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # フォーマッタの作成
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # ルートロガーの設定
    logger = logging.getLogger("mcp_server")
    logger.setLevel(level)

    # コンソールハンドラー
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # ファイルハンドラー　（日付ごとにローテーション）
    if log_to_file:
        log_file = log_dir / f"mcp-server-{datetime.now().strftime('%Y%m%d')}.log"
        file_handler = logging.handlers.RotatingFileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


logger = setup_logging(level="DEBUG")
