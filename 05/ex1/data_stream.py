#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Dict, Union, List, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = "Generic stream"

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return ([d for d in data_batch if criteria is None
                 or (isinstance(d, str) and d in criteria)])

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"
        self.criteria = ["temp", "humidity", "pressure"]

    def process_batch(self, data_batch: List[Any]) -> str:
        readings = self.filter_data(data_batch, self.criteria)
        if len(readings) == 0:
            return "0 readings processed"

        total_val_count, total_tmp, avg_tmp, n = 0, 0, 0, 0
        for data in readings:
            r, v = data.split(":", 1)
            match r:
                case "temp":
                    total_tmp += float(v)
                    total_val_count += 1
                    n += 1
                case "pressure":
                    n += 1
                case "humidity":
                    n += 1
        if total_val_count > 0:
            avg_tmp = total_tmp / total_val_count
        return f"{n} readings processed, avg temp: {avg_tmp}°C"

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            filtered_data = [
                d for d in data_batch if isinstance(d, str) and ":" in d
                and d.split(":")[0] in criteria
                and (d.split(":")[1]
                     .strip()
                     .replace('-', '', 1)
                     .replace('.', '', 1)
                     .isdigit())
            ]
            return filtered_data
        except Exception:
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["name"] = "Sensor Stream"
        stats["data_type"] = "Sensor Data"
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"
        self.criteria = ["buy", "sell"]

    def process_batch(self, data_batch: List[Any]) -> str:
        ops = self.filter_data(data_batch, self.criteria)
        net_flow, n = 0, 0
        for data in ops:
            action, value = data.split(":", 1)
            match action:
                case "buy":
                    net_flow += int(value)
                    n += 1
                case "sell":
                    net_flow -= int(value)
                    n += 1
        return (f"{n} operations, " + "net flow: {0:+} units".format(net_flow))

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            filtered_data = [
                d for d in data_batch if isinstance(d, str) and ":" in d
                and d.split(":")[0] in criteria
                and (d.split(":")[1]
                     .strip()
                     .replace('-', '', 1)
                     .replace('.', '', 1)
                     .isdigit())
            ]
            return filtered_data
        except Exception:
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["name"] = "Transaction Stream"
        stats["data_type"] = "Transaction data"
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"
        self.criteria = ["error", "login", "logout"]

    def process_batch(self, data_batch: List[Any]) -> str:
        filtered_data = self.filter_data(data_batch, self.criteria)
        err_count, n = 0, 0
        for data in filtered_data:
            match data:
                case "error":
                    err_count += 1
                    n += 1
                case "login":
                    n += 1
                case "logout":
                    n += 1
        return (f"{n} events, {err_count} error"
                f"{'' if err_count < 2 else 's'} detected")

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            filtered_data = [
                d for d in data_batch if isinstance(d, str)
                and ":" not in d and d in criteria
            ]
            return filtered_data
        except Exception:
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["name"] = "Event Stream"
        stats["data_type"] = "Event Data"
        return stats


class StreamProcessor:
    @staticmethod
    def process_stream_batch(streams: List[DataStream],
                             data: List[Any]) -> None:
        for s in streams:
            try:
                result = s.process_batch(data)
                print(f"- {s.get_stats().get('data_type')}: {result}")
            except Exception as e:
                print("Error processing stream "
                      f"{s.get_stats().get('stream_id')}: {e}")

    @staticmethod
    def filter_stream_batch(streams: List[DataStream],
                            data_batch: List[Any]) -> None:
        print("Stream filtering active: High-priority data only")
        crit_alerts, large_trans = 0, 0
        for s in streams:
            data = s.filter_data(data_batch, s.criteria)
            for d in data:
                if d == "error":
                    crit_alerts += 1
                elif ":" in d:
                    action, val = d.split(":")
                    if action in ["buy", "sell"] and float(val) > 150:
                        large_trans += 1
        return (f"{crit_alerts} critical sensor alerts, "
                f"{large_trans} large transaction"
                f"{'' if large_trans < 2 else 's'}")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensors = [SensorStream("SENSOR_001"),
               TransactionStream("TRANS_001"),
               EventStream("EVENT_001")]
    data_batches = [["temp:22.5", "humidity:65", "pressure:1013", "temp:23.5"],
                    ["buy:100", "sell:150", "buy:75"],
                    ["login", "error", "logout"]]

    for sensor, data in zip(sensors, data_batches):
        print(f"Initializing {sensor.get_stats().get('name')}")
        print(f"Stream ID: {sensor.get_stats().get('stream_id')}, "
              f"Type: {sensor.get_stats().get('stream_type')}")
        print(f"Processing sensor batch: [{', '.join(data)}]")
        print(f"Sensor analysis: {sensor.process_batch(data)}")
        print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed streams types through unified interface...\n")

    streams = [SensorStream("SENSOR_002"),
               TransactionStream("TRANS_002"),
               EventStream("EVENT_002")]
    data = ["temp:23.5", "logout", "error", "sell:200",
            "buy:100", "login", "temp:24.5", "error",
            "buy:50", "humidity:70"]

    print("Batch 1 results:")
    StreamProcessor.process_stream_batch(streams, data)
    print()

    print(f"Filtered results: "
          f"{StreamProcessor.filter_stream_batch(streams, data)}")

    print("\nAll streams processed successfully. Nexus throughput optimal")
