import os
#run a sql file

#cmd_run_sql = f'psql -f {name}.sql "dbname=postgres user=postgres password=example host=127.0.0.1"'

cmd_dump = f'pg_dump -d learn --schema=scenario_基辅口袋_judge -t deploy -U postgres -W example -h 127.0.0.1'
cmd_connect = f'psql "dbname=postgres user=postgres password=example host=127.0.0.1"'

def run_sql(name):
    os.system()


def main():
    #run_sql('newdb')
    #run_sql('hello')
    os.system(f'{cmd_dump} | {cmd_connect}')

if __name__ == '__main__':
    main()