from pathlib import Path

# Logger 名称
LOGGER_NAME = 'judger'
# CPU 时间限制，单位纳秒 (10 秒)
DEFAULT_TIME_LIMIT = 10_000_000_000
# 内存限制，单位 Byte (256MB)
DEFAULT_MEMORY_LIMIT = 256 * 1024 * 1024
# 线程数量限制
DEFAULT_PROC_LIMIT = 64
# CPU 使用率限制，1000 等于单核 100%
DEFAULT_CPU_RATE_LIMIT = 1000
# 输出限制，单位 Byte (8MB)
DEFAULT_OUTPUT_LIMIT = 8 * 1024 * 1024
# 默认检查器
DEFAULT_CHECKER = Path(__file__).parent / 'checkers' / 'default.cpp'
