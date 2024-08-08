import psutil
import time
import logging

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80.0  # percentage
MEMORY_THRESHOLD = 80.0  # percentage
DISK_THRESHOLD = 80.0  # percentage
PROCESS_THRESHOLD = 200  # number of processes

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alert(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        alert(f"High memory usage detected: {memory_usage}%")
    return memory_usage

def check_disk_space():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        alert(f"Low disk space detected: {disk_usage}% used")
    return disk_usage

def check_running_processes():
    processes = len(psutil.pids())
    if processes > PROCESS_THRESHOLD:
        alert(f"High number of running processes detected: {processes}")
    return processes

def alert(message):
    print(message)
    logging.info(message)

def main():
    while True:
        cpu_usage = check_cpu_usage()
        memory_usage = check_memory_usage()
        disk_usage = check_disk_space()
        processes = check_running_processes()
        
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")
        print(f"Disk Usage: {disk_usage}%")
        print(f"Running Processes: {processes}")
        
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    main()