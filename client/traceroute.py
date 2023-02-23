import subprocess

def run_traceroute(destination):
    cmd = ["traceroute", destination]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def run_ping(destination):
    cmd = ["ping", "-c 5", destination]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout