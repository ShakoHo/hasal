# Hasal New Agent

## Running

```bash
$ python ejenti.py
```

The agent can be triggered by a json format configuration file. You need to put the file path in to make sure the agent can be triggered automatically.


## Config

The config file structure:

* config.json
```json
{
  "job_store_url": "sqlite:///job_store.db",
  "interactive_cmd_polling_interval": 5,
  "log_level": "debug",
  "log_filter": [
    "apscheduler.executors.default",
    "apscheduler.scheduler"
  ]
}
```

* pulse_config.json
```json
{
  "pulse_username": "<PULSE_USERNAME>",
  "pulse_password": "<PULSE_PASSWORD>"
}
```

* job_config.json
```json
{
  "async_tasks_consumer": {
    "module-path": "jobs.tasks_consumer",
    "trigger-type": "interval",
    "interval": 3,
    "max-instances": 1,
    "default-loaded": true,
    "configs": {}
  },
  "sync_tasks_consumer": {
    "module-path": "jobs.tasks_consumer",
    "trigger-type": "interval",
    "interval": 3,
    "max-instances": 1,
    "default-loaded": true,
    "configs": {}
  },
  "listen_pulse": {
    "module-path": "jobs.pulse",
    "trigger-type": "interval",
    "interval": 0,
    "max-instances": 1,
    "default-loaded": true,
    "configs": {
      "username": "<PULSE_USERNAME>",
      "password": "<PULSE_PASSWORD>"
    }
  }
}
```

* cmd_config.json
```json
{
  "cmd-settings": {
    "del-job": {
      "desc": "delete a existing job",
      "func-name": "scheduler_del_job",
      "configs": {}
    },
    "list-job": {
      "desc": "list the current jobs",
      "func-name": "scheduler_list_job",
      "configs": {}
    },
    "help": {
      "desc": "list all support commands",
      "func-name": "list_all_commands",
      "configs": {}
    },
    "exit": {
      "desc": "graceful shutdown this agent",
      "func-name": "scheduler_shutdown",
      "configs": {}
    },
    "run-hasal-on-latest-nightly": {
      "desc": "run hasal test on latest nightly, which will include download nightly and deploy it",
      "module-path": "tasks.hasalTasks",
      "func-name": "run_hasal_on_latest_nightly",
      "queue-type": "sync",
      "configs": {}
    },
    "download-latest-nightly": {
      "desc": "download the latest nightly and return the dl pkg path and json path",
      "module-path": "tasks.firefoxBuildTasks",
      "func-name": "download_latest_nightly_build",
      "queue-type": "sync",
      "configs": {}
    },
    "deploy-fx-package": {
      "desc": "deploy downloaded firefox package in your system, need to specify dl pkg path after your cmd",
      "module-path": "tasks.firefoxBuildTasks",
      "func-name": "deploy_fx_package",
      "queue-type": "sync",
      "configs": {}
    },
    "git-pull": {
      "desc": "git pull remote branch",
      "module-path": "tasks.githubTasks",
      "func-name": "git_pull",
      "queue-type": "sync",
      "configs": {}
    },
    "git-checkout": {
      "desc": "git checkout revision/branch",
      "module-path": "tasks.githubTasks",
      "func-name": "git_checkout",
      "queue-type": "sync",
      "configs": {}
    },
    "git-fetch": {
      "desc": "git fetch remote",
      "module-path": "tasks.githubTasks",
      "func-name": "git_fetch",
      "queue-type": "sync",
      "configs": {}
    },
    "git-reset": {
      "desc": "git reset --hard HEAD",
      "module-path": "tasks.githubTasks",
      "func-name": "git_reset",
      "queue-type": "sync",
      "configs": {}
    },
    "generate-hasal-config": {
      "desc": "generate hasal configs for ejenti",
      "module-path": "tasks.hasalTasks",
      "func-name": "generate_hasal_config",
      "queue-type": "sync",
      "configs": {}
    },
    "exec-hasal-runtest": {
      "desc": "wrapper to direct call runtest",
      "module-path": "tasks.hasalTasks",
      "func-name": "exec_hasal_runtest",
      "queue-type": "sync",
      "configs": {}
    }
  }
}
```

