from dataclasses import dataclass, field
from typing import List, Dict

from .models import Language


@dataclass
class LanguageConfig:
    source_filename: str
    compiled_filename: str
    need_compile: bool
    compile_cmd: List[str]
    run_cmd: List[str]
    time_factor: int = field(default=1)
    memory_factor: int = field(default=1)


class LanguageRegistry:
    _mapping: Dict[Language, LanguageConfig] = {}

    @classmethod
    def register(cls, lang: Language, config: LanguageConfig) -> None:
        if lang in cls._mapping:
            raise ValueError("Language %s is already registered" % lang)
        cls._mapping[lang] = config

    @classmethod
    def get_config(cls, lang: Language) -> LanguageConfig:
        if lang not in cls._mapping:
            raise ValueError("Language %s is not registered" % lang)
        return cls._mapping[lang]


LanguageRegistry.register(
    Language.C,
    LanguageConfig(
        source_filename="Main.c",
        compiled_filename="Main",
        need_compile=True,
        compile_cmd=[
            "/usr/bin/gcc-12", "Main.c", "-o", "Main",
            "-std=c11", "-O2", "-lm", "-DONLINE_JUDGE",
            "-w", "-fmax-errors=3", "--static"
        ],
        run_cmd=[
            "./Main"
        ]
    )
)

LanguageRegistry.register(
    Language.Cpp11,
    LanguageConfig(
        source_filename="Main.cpp",
        compiled_filename="Main",
        need_compile=True,
        compile_cmd=[
            "/usr/bin/g++-12", "Main.cpp", "-o", "Main",
            "-std=c++11", "-O2", "-lm", "-DONLINE_JUDGE",
            "-w", "-fmax-errors=3", "--static"
        ],
        run_cmd=[
            "./Main"
        ]
    )
)

LanguageRegistry.register(
    Language.Cpp17,
    LanguageConfig(
        source_filename="Main.cpp",
        compiled_filename="Main",
        need_compile=True,
        compile_cmd=[
            "/usr/bin/g++-12", "Main.cpp", "-o", "Main",
            "-std=c++17", "-O2", "-lm", "-DONLINE_JUDGE",
            "-w", "-fmax-errors=3", "--static"
        ],
        run_cmd=[
            "./Main"
        ]
    )
)

LanguageRegistry.register(
    Language.Java,
    LanguageConfig(
        source_filename="Main.java",
        compiled_filename="Main.jar",
        need_compile=True,
        compile_cmd=[
            "/usr/bin/bash", "-c", " ".join([
                "/usr/bin/javac", "Main.java", "-encoding", "UTF-8", "&&",
                "/usr/bin/jar", "cvf", "Main.jar", "*.class"
            ])
        ],
        run_cmd=[
            "/usr/bin/java", "-DONLINE_JUDGE", "-cp", "Main.jar", "Main"
        ],
        time_factor=2,
        memory_factor=2
    )
)

LanguageRegistry.register(
    Language.Python,
    LanguageConfig(
        source_filename="Main.py",
        compiled_filename="Main.pyc",
        need_compile=True,
        compile_cmd=[
            "/usr/bin/bash", "-c", " ".join([
                "/usr/bin/python3.11", "-m", "py_compile", "Main.py", "&&",
                "mv", "__pycache__/Main.cpython-311.pyc", "Main.pyc"
            ])
        ],
        run_cmd=[
            "/usr/bin/env", "ONLINE_JUDGE=1",
            "/usr/bin/python3.11", "Main.pyc"
        ]
    )
)

LanguageRegistry.register(
    Language.PHP8_2,
    LanguageConfig(
        source_filename="Main.php",
        compiled_filename="Main.php",
        need_compile=False,
        compile_cmd=[],
        run_cmd=[
            "/usr/bin/env", "ONLINE_JUDGE=1",
            "/usr/bin/php8.2", "Main.php"
        ],
        time_factor=2,
        memory_factor=2
    )
)

# JavaScript (Node.js)
LanguageRegistry.register(
    Language.JavaScript,
    LanguageConfig(
        source_filename="Main.js",
        compiled_filename="Main.js",
        need_compile=False,
        compile_cmd=[],
        run_cmd=[
            "/usr/bin/env", "ONLINE_JUDGE=1",
            "/usr/bin/node", "Main.js"
        ],
        time_factor=2,
        memory_factor=2
    )
)

# LanguageRegistry.register(
#     Language.TypeScript,
#     LanguageConfig(
#         source_filename="Main.ts",
#         compiled_filename="Main.js",
#         need_compile=True,
#         compile_cmd=[
#             "tsc", "Main.ts", "--outFile", "Main.js"
#         ],
#         run_cmd=[
#             "/usr/bin/env", "ONLINE_JUDGE=1",
#             "/usr/bin/node", "Main.js"
#         ],
#         time_factor=2,
#         memory_factor=2
#     )
# )