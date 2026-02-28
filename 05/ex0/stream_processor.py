#!/usr/bin/env python3

from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        """Process data depending on its type"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate data depending on its type"""
        pass

    def format_output(self, result: str) -> str:
        """Format result output for printing"""
        return f"Processed {result}"


class NumericProcessor(DataProcessor):
    def __init__(self):
        self.__name__ = "Numeric Processor"

    def process(self, data: Any) -> str:
        if self.validate(data) is True:
            num_values = len(data)
            data_sum = sum(data)
            data_avg = round(data_sum / num_values, 2)
            result = (f"{num_values} numeric values, "
                      f"sum={data_sum}, avg={data_avg}")
            return self.format_output(result)
        else:
            return ""

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, list):
                raise TypeError
            for d in data:
                if not isinstance(d, (int, float)):
                    raise TypeError
            return True
        except TypeError:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def __init__(self):
        self.__name__ = "Text Processor"

    def process(self, data: Any) -> str:
        if self.validate(data) is True:
            char_count = len(data)
            word_count = len(data.split(" "))
            result = f"text: {char_count} characters, {word_count} words"
            return self.format_output(result)
        else:
            return ""

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                raise TypeError
            if ": " in data:
                raise TypeError
            return True
        except TypeError:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def __init__(self):
        self.__name__ = "Log Processor"

    def process(self, data: Any) -> str:
        if self.validate(data) is True:
            log_level, message = data.split(": ", 1)
            result = f"[ALERT] {log_level} level detected: {message}"
            return self.format_output(result)
        else:
            return ""

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                raise TypeError
            if ": " not in data:
                raise ValueError
            return True
        except (TypeError, ValueError):
            return False

    def format_output(self, result: str) -> str:
        return result


def interface(processor: List, data: Any) -> None:
    for p in processor:
        res = p.process(data)
        if res != "":
            return res


def test(processor: DataProcessor, data: Any) -> None:
    print(f"Initializing {processor.__name__}...")
    print(f"Processing data: {data}")
    print(f"Validation: {processor.validate(data)}")
    print(f"Output: {processor.process(data)}\n")


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    data = [
        [1, 2, 3, 4, 5],
        "Hello Nexus world",
        "ERROR: Connection timeout"
    ]

    for p, d in zip(processors, data):
        test(p, d)

    print("=== Polymorphic Processing Demo ===")

    print("Processing multiple data through some interface...")
    for i, d in enumerate(data, 1):
        print(f"Result {i}: {interface(processors, d)}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")
