🚀 Apache Airflow Learning & Orchestration Project

This project contains a collection of Apache Airflow DAGs demonstrating core and advanced orchestration patterns including scheduling strategies, task branching, XCom usage, dynamic task mapping, assets (data-aware scheduling), incremental loads, and cross-DAG orchestration using TriggerDagRunOperator.

It is designed as a hands-on Airflow practice and reference project for building production-style data pipelines.

📂 Project Structure
AIRFLOW/
├── config/
│   └── airflow.cfg
├── dags/
│   ├── 1_first_dag.py
│   ├── asset_1.py
│   ├── asset_2.py
│   ├── branches.py
│   ├── dag_orchestrator_parent.py
│   ├── dag_orchestrator_1.py
│   ├── dag_orchestrator_2.py
│   ├── incremental_load.py
│   ├── parallel_tasks.py
│   ├── schedule_cron.py
│   ├── schedule_delta.py
│   ├── schedule_preset.py
│   ├── special_dates.py
│   ├── xcom_auto.py
│   └── xcom_manual.py
├── logs/
├── plugins/
├── docker-compose.yaml
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md

🎯 Key Concepts Demonstrated

This project covers:

✅ Core DAG Basics

First DAG creation

Task dependencies

Operators and TaskFlow API

DAG parameters and structure

File: 1_first_dag.py

⏱ Scheduling Patterns

Different Airflow scheduling mechanisms:

Cron Scheduling

Custom cron expressions

File: schedule_cron.py

Timedelta Scheduling

Interval-based scheduling

File: schedule_delta.py

Preset Schedules

@daily, @hourly, etc.

File: schedule_preset.py

Special Date Logic

Custom calendar/date-based triggers

File: special_dates.py

🔀 Branching Logic

Conditional task execution using Branch operators.

File: branches.py

Features:

Conditional flow control

Selective downstream execution

Skip behavior handling

⚡ Parallel Task Execution

Running tasks concurrently and joining flows.

File: parallel_tasks.py

Concepts:

Parallel branches

Fan-out / fan-in patterns

🔁 XCom Patterns
Automatic XCom (TaskFlow API)

File: xcom_auto.py

Return values auto-pushed

Clean Pythonic pattern

Manual XCom

File: xcom_manual.py

Explicit push/pull

Key/value control

📦 Assets / Data-Aware Scheduling

Demonstrates Airflow asset-based triggering (data-driven DAG scheduling).

Files:

asset_1.py

asset_2.py

Concepts:

Dataset/Asset definitions

Producer DAGs

Consumer DAGs triggered by asset updates

Cross-DAG data dependencies

🔗 Cross-DAG Orchestration

Parent DAG triggering child DAGs.

Files:

dag_orchestrator_parent.py

dag_orchestrator_1.py

dag_orchestrator_2.py

Concepts:

TriggerDagRunOperator

Multi-DAG workflows

Modular orchestration design

📈 Incremental Load Pattern

Incremental data processing workflow.

File: incremental_load.py

Concepts:

Incremental extraction logic

Stateful processing

Partition/time-based loads

Dynamic task mapping patterns

🐳 Running with Docker

This project includes a Docker Compose setup for running Airflow locally.

Start Airflow
docker compose up -d

Initialize Airflow (first time)
docker compose run airflow-init

Access UI
http://localhost:8080


Default credentials (if unchanged):

username: airflow
password: airflow

🧪 How to Test DAGs

Start containers

Open Airflow UI

Enable DAG

Trigger manually

Inspect:

Graph View

Grid View

Task logs

XCom tab

Asset view (for asset DAGs)

🧰 Tech Stack

Apache Airflow v3

Python

Docker & Docker Compose

TaskFlow API

Dynamic Task Mapping

Asset Scheduling

Cross-DAG orchestration

📚 Learning Goals Covered

This project demonstrates practical usage of:

DAG design patterns

Scheduling strategies

Branching & conditional flows

Parallelism

XCom communication

Asset-driven pipelines

Incremental processing

Parent-child DAG orchestration

Modern Airflow v3 operator imports

🚧 Notes

logs/ is ignored from git

.env is excluded for security

__pycache__ excluded

Config can be templated for production use

Designed for learning + portfolio demonstration