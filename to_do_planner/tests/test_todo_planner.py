import os
import sys
import unittest
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from planner import sorted_view, status_of
from tasks import create_task, find_task


class TaskTests(unittest.TestCase):
    def setUp(self):
        self.tasks = []
        create_task(self.tasks, "Assignment", (date.today() - timedelta(days=2)).isoformat(), 1)
        create_task(self.tasks, "Reading", (date.today() + timedelta(days=1)).isoformat(), 2)
        create_task(self.tasks, "Project", (date.today() + timedelta(days=10)).isoformat(), 3)

    def test_ids_increase(self):
        self.assertEqual([t["id"] for t in self.tasks], [1, 2, 3])

    def test_find_task(self):
        self.assertEqual(find_task(self.tasks, 2)["title"], "Reading")
        self.assertIsNone(find_task(self.tasks, 99))

    def test_status_overdue(self):
        self.assertTrue(status_of(self.tasks[0]).startswith("OVERDUE"))

    def test_status_due_soon(self):
        self.assertTrue(status_of(self.tasks[1]).startswith("due in"))

    def test_status_upcoming(self):
        self.assertEqual(status_of(self.tasks[2]), "upcoming")

    def test_sorted_view_pending_only(self):
        self.tasks[0]["done"] = True
        pending = sorted_view(self.tasks, only_pending=True)
        self.assertEqual(len(pending), 2)


if __name__ == "__main__":
    unittest.main()
