#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Dict, Union, List, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = "Generic stream"

    @property
    def stream_id(self) -> None:
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id: str) -> None:
        self._stream_id: str = stream_id

    @property
    def stream_type(self) -> str:
        return self._stream_type

    @stream_type.setter
    def stream_type(self, stream_type: str) -> None:
        self._stream_type = stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return Dict(self.stream_id, self.stream_type)


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.__name__ = "Sensor Stream"
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing sensor batch: {data_batch}")
        data_batch = self.filter_data(data_batch)
        try:
            n = len(data_batch)
            count, total_tmp = 0, 0
            for data in data_batch:
                parsed_data = data.split(":", 1)[0]
                if parsed_data[0] == "temp":
                    total_tmp += parsed_data[1]
                    count += 1
            avg_tmp = total_tmp / count
        except (TypeError, ValueError):
            return "Error while parsing data"
        return f"{n} readings processed, avg. temp: {avg_tmp}"

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return Dict(self.stream_id, self.stream_type)


class TransactionStream(DataStream):
    pass


class EventStream(DataStream):
    pass


class StreamProcessor:
    def process_stream_batch(self,
                             stream: DataStream,
                             data: List[Any]) -> None:
        print(f"Initializing {stream.__name__}...")
        print(f"Stream ID: {stream.stream_id}, Type: {stream.stream_type}")
        result = stream.process_batch(data)
        print(f"Output: {result}")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    """Sensor Stream test"""
    sensor = SensorStream("SENSOR_001")
    data = ["temp:22.5", "humidity:65", "pressure:1013", "temp:23.5"]
    sensor.process_batch(data)

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed streams types through unified interface...")

    manager = StreamProcessor()
    sensors = [SensorStream(), TransactionStream(), EventStream()]
    data = []

    for s in sensors:
        manager.process_stream_batch(s, data)

    print("\nAll streams processed successfully. Nexus throughput optimal")
