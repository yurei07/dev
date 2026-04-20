############################# DETECLASSES ################################

# from dataclasses import dataclass
#
# @dataclass
# class User:
#     age: int
#     name: str
#
#     def greet(self) -> str:
#         return f"Hello, my name is {self.name} and I am {self.age} years old."
#
# user = User(age = 25, name = "Nazarii")
# print(user.greet())
# print(user)


############################### ARGPARSE ################################

# import argparse 

# parser.add_argument("--name", type=str, help="Name", required=True)
#
# parser.add_argument("--age", type=int, help="Age", default=0)
# args = parser.parse_args()
#
# print(f"Hello {args.name}. I'm {args.age} years old!")


############################### PSUTIL ##############################

# import psutil
#
# psutil.cpu_percent(interval=1)
# psutil.virtual_memory()
# psutil.disk_usage("/")



############################# PROJECT #####################################

from dataclasses import dataclass 
import argparse 
import psutil

@dataclass 
class CpuInfo:
    percent: float

    def get_cpu(self) -> str:
        return f"CPU: {self.percent}%"

@dataclass
class MemoryInfo:
    percent: float
    used: float
    total: float


    def get_memory(self) -> str:
        return f"Memory: {self.used:.2f} GB total / {self.total:.2f} GB used ({self.percent}%)"

@dataclass 
class DiskInfo:
    percent: float
    used: float
    total: float

    def get_disk(self) -> str:
        return f"Disk: {self.used:.2f} GB total / {self.total:.2f} GB used ({self.percent}%)"


parser = argparse.ArgumentParser()

parser.add_argument("--cpu", help="Info about CPU", action='store_true')
parser.add_argument("--memory", help="Info about Memory", action="store_true")
parser.add_argument("--disk", help="Info about Disk", action="store_true")

parser.add_argument("--all", help="Info about CPU Memory and Disk", action="store_true")

args = parser.parse_args()
gb = 1024 * 1024 *1024

if args.all:
    args.cpu = True
    args.memory = True
    args.disk = True
    # cpu = psutil.cpu_percent(interval=1)
    # ram = psutil.virtual_memory()
    # disk = psutil.disk_usage("/")
    #
    # infoCpu = CpuInfo(cpu)
    # infoRam = MemoryInfo(ram.percent, ram.total / gb, ram.used / gb)
    # infoDisk = DiskInfo(disk.percent, disk.total / gb, disk.used / gb)

    # print(infoCpu.get_cpu())
    # print(infoRam.get_memory())
    # print(infoDisk.get_disk())

if args.cpu:
    raw = psutil.cpu_percent(interval=1)
    info = CpuInfo(raw)
    print(info.get_cpu())

if args.memory:
    raw = psutil.virtual_memory()
    info = MemoryInfo(raw.percent, raw.total / gb, raw.used / gb)
    print(info.get_memory())

if args.disk:
    raw = psutil.disk_usage("/")
    info = DiskInfo(raw.percent, raw.total / gb, raw.used / gb)
    print(info.get_disk())

