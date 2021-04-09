import sys
import json
import yaml
from cprint import cprint
from modules.run import GoThread
from modules.detect import detect
from modules.report import Reporter

def main():

  with open('./config.yaml') as f:
    config = yaml.load(f, Loader=yaml.SafeLoader)  # Read config
    if config:
      cprint.ok("load config is " + json.dumps(config))
    else:
      cprint.fatal("load config file `config.yaml` failed")

  reporter = Reporter(config.get("report_url"), config.get("interval"), config.get("street"))
  detect(config.get("source"), config.get("device"), config.get("keys"), reporter)

  # threads = []
  # for source in config.get("sources"):
  #   t = GoThread("Thread for "+source, source, config.get("device"))
  #   t.start()
  #   threads.append(t)
  
  # # 等待所有线程完成
  # for t in threads:
  #   t.join()

if __name__ == "__main__":
  main()