#!/usr/bin/env python3

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> bool:
        """Process data depending on its type"""
        pass

    @abstractmethod
    def validate(self, data: str) -> bool:
        """Validate data depending on its type"""
        pass

    def format_output(self, result: str) -> str:
        """Format result output for printing"""
        return f"Processed {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> bool:
        print("Initializing Numeric Processor...")
        print("Processing data:", data)
        if self.validate(data) is True:
            num_values = len(data)
            data_sum = sum(data)
            data_avg = round(data_sum / num_values, 2)
            result = (f"{num_values} numeric values, "
                      f"sum={data_sum}, avg={data_avg}")
            print(self.format_output(result))
        else:
            pass

    def validate(self, data: str) -> bool:
        try:
            if type(data) is not list:
                raise TypeError
            for d in data:
                int(d)
            print("Numeric data verified")
            return True
        except (TypeError, ValueError):
            print("Not numeric data")
            return False


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> bool:
        print("Initializing Text Processor...")
        print(f"Processing data: \"{data}\"")
        if self.validate(data) is True:
            char_count = len(data)
            word_count = len(data.split(" "))
            result = f"text: {char_count} characters, {word_count} words"
            print(self.format_output(result))
        else:
            pass

    def validate(self, data: str) -> bool:
        try:
            str(data)
            print("Text data verified")
            return True
        except (TypeError, ValueError):
            print("Not text data")
            return False


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> bool:
        print("Initializing Log Processor...")
        print(f"Processing data: \"{data}\"")
        print("TODO")

    def validate(self, data: str) -> bool:
        try:
            if data[:5] != "ERROR":
                raise TypeError
            return f"[ALERT] ERROR level detected: {data[5:]}"
        except (TypeError, ValueError):
            return "Not log data"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    numeric_data = [1, 2, 3, 4, 5]
    text_data = "Hello Nexus world"
    log_data = "ERROR: Connection timeout"

    numeric_proc = NumericProcessor()
    numeric_proc.process(numeric_data)
    print()
    text_proc = TextProcessor()
    text_proc.process(text_data)
    print()
    log_proc = LogProcessor()
    log_proc.process(log_data)

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple ata through some interface...")
