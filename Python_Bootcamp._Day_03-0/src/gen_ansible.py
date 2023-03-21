import yaml


class MyDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)


with open('../materials/todo.yml', 'r') as f:
    todo = yaml.safe_load(f)

server_packages = todo['server']['install_packages']
exploit_files = todo['server']['exploit_files']
bad_guys = todo['bad_guys']

deploy = {
    'hosts': 'webserver',
    'become': True,
    'tasks': [
                 {
                     'name': 'Install packages',
                     'apt': 'name={pkg} state=present'.format(pkg=pkg)
                 } for pkg in server_packages
             ] + [
                 {
                     'name': 'Copy exploit files',
                     'copy': 'src={file} dest=/home/ubuntu/{file} mode=0644'.format(file=file)
                 } for file in exploit_files
             ] + [
                 {
                     'name': 'Run exploit.py on remote server with bad_guys argument',
                     'command': 'python3 /home/ubuntu/exploit.py -e {bg}'.format(bg=','.join(bad_guys))
                 },
                 {
                     'name': 'Run consumer.py on remote server',
                     'command': 'python3 /home/ubuntu/consumer.py'
                 }
             ]
}

with open('deploy.yml', 'w') as f:
    yaml.dump(deploy, f, Dumper=MyDumper, default_flow_style=False)
