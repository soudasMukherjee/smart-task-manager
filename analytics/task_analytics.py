import numpy as np
import pandas as pd


def compute_analytics(tasks):
    """tasks: list[Task]"""
    rows = [
        {
            "status": t.status,
            "priority": t.priority,
            "created_at": t.created_at,
        }
        for t in tasks
    ]

    df = pd.DataFrame(rows)

    total_tasks = int(len(df))

    # Handle empty DataFrame safely
    if total_tasks == 0:
        completed_tasks = 0
        pending_tasks = 0
        completion_percentage = 0.0
    else:
        status_np = np.array(df["status"].tolist())

        completed_tasks = int(np.sum(status_np == "Done"))
        pending_tasks = int(np.sum(status_np != "Done"))
        completion_percentage = float((completed_tasks / total_tasks) * 100.0)

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "completion_percentage": round(completion_percentage, 2),
    }

