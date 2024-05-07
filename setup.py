import configparser
import subprocess

def run_nginx_server():
    config = configparser.ConfigParser()
    config.read('IMServer.ini')
    nginx_exec = config.get('nginx', 'exec')
    print("nginx exec:", nginx_exec)
    print("run nginx server.")
    subprocess.run([nginx_exec, '-s', 'stop'])
    subprocess.run([nginx_exec, '-c', 'conf/nginx.conf'], check=True)
    


if __name__ == "__main__":
    run_nginx_server()